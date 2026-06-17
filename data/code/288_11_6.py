import math
def convert_temperature(temp, source_scale):
    if source_scale == "Celsius":
        celsius = temp
        fahrenheit = (celsius * 9/5) + 32
        kelvin = celsius + 273.15
        return {"Celsius": celsius, "Fahrenheit": fahrenheit, "Kelvin": kelvin}
    elif source_scale == "Fahrenheit":
        fahrenheit = temp
        celsius = (fahrenheit - 32) * 5/9
        kelvin = celsius + 273.15
        return {"Celsius": celsius, "Fahrenheit": fahrenheit, "Kelvin": kelvin}
    elif source_scale == "Kelvin":
        kelvin = temp
        celsius = kelvin - 273.15
        fahrenheit = (celsius * 9/5) + 32
        return {"Celsius": celsius, "Fahrenheit": fahrenheit, "Kelvin": kelvin}
    else:
        raise ValueError("Unsupported source scale")
if __name__ == '__main__':
    test_temp = 20.0
    test_scale = "Celsius"
    results = convert_temperature(test_temp, test_scale)
    print(f"Source: {test_temp}°C")
    print(f"Results: {results}")
    test_temp = 68.0
    test_scale = "Fahrenheit"
    results = convert_temperature(test_temp, test_scale)
    print(f"\nSource: {test_temp}°F")
    print(f"Results: {results}")
    test_temp = 300.15
    test_scale = "Kelvin"
    results = convert_temperature(test_temp, test_scale)
    print(f"\nSource: {test_temp}K")
    print(f"Results: {results}")