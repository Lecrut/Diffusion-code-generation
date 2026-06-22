def convert_temperature(value, from_scale):
    if from_scale == "Fahrenheit":
        celsius = (value - 32) * 5/9
        kelvin = celsius + 273.15
        reaumur = celsius * 4/5
        rankine = value + 459.67
    elif from_scale == "Celsius":
        fahrenheit = value * 9/5 + 32
        kelvin = value + 273.15
        reaumur = value * 4/5
        rankine = (value * 9/5) + 491.67
    elif from_scale == "Kelvin":
        fahrenheit = (value - 273.15) * 9/5 + 32
        celsius = value - 273.15
        reaumur = (value - 273.15) * 4/5
        rankine = (value - 273.15) * 9/5
    elif from_scale == "Réaumur":
        fahrenheit = (value * 25/100) * 9/5 + 32
        celsius = value * 5/4
        kelvin = celsius + 273.15
        rankine = (celsius * 9/5) + 491.67
    elif from_scale == "Rankine":
        fahrenheit = value - 459.67
        celsius = (value - 491.67) * 5/9
        kelvin = (value - 491.67) * 5/9 + 273.15
        reaumur = (celsius * 4/5)
    else:
        raise ValueError("Invalid temperature scale")

    return {
        "Fahrenheit": fahrenheit,
        "Celsius": celsius,
        "Kelvin": kelvin,
        "Réaumur": reaumur,
        "Rankine": rankine
    }

if __name__ == '__main__':
    temp_fahrenheit = 77.0
    converted_temps = convert_temperature(temp_fahrenheit, "Fahrenheit")
    print(f"Fahrenheit: {temp_fahrenheit}°F is {converted_temps}")