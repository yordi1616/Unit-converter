from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    input_value = None
    input_unit = None
    output_unit = None
    error = None

    if request.method == 'POST':
        try:
            input_value = float(request.form['value'])
            input_unit = request.form['input_unit']
            output_unit = request.form['output_unit']

            # Make sure input and output units are different
            if input_unit == output_unit:
                error = "እባክዎ የተለያዩ የመለኪያ አይነቶችን ይምረጡ።"
            
            # Perform conversions
            elif input_unit == 'celsius' and output_unit == 'fahrenheit':
                result = (input_value * 9/5) + 32
                result = f"{input_value}°C = {result:.2f}°F"
            elif input_unit == 'fahrenheit' and output_unit == 'celsius':
                result = (input_value - 32) * 5/9
                result = f"{input_value}°F = {result:.2f}°C"
            elif input_unit == 'km' and output_unit == 'miles':
                result = input_value * 0.621371
                result = f"{input_value} km = {result:.2f} miles"
            elif input_unit == 'miles' and output_unit == 'km':
                result = input_value / 0.621371
                result = f"{input_value} miles = {result:.2f} km"
            else:
                error = "የተመረጡት የመለኪያ አይነቶች ትክክል አይደሉም።"

        except ValueError:
            error = "እባክዎ ትክክለኛ ቁጥር ያስገቡ።"
        except Exception as e:
            error = f"ስህተት ተፈጥሯል: {e}"

    # Pass current values back to the template to keep them in the form
    return render_template('index.html', result=result, error=error, 
                           input_value=input_value, input_unit=input_unit, output_unit=output_unit)

if __name__ == '__main__':
    app.run(debug=True)
