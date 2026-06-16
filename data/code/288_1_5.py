import math
def convert_temp(temp, source_scale):
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
    test_source = "Celsius"
    results = convert_temp(test_temp, test_source)
    print(f"Source: {test_source}, Temperature: {test_temp}")
    print("Results:")
    for scale, value in results.items():
        print(f"{scale}: {value:.2f}")
    test_temp = 68.0
    test_source = "Fahrenheit"
    results = convert_temp(test_temp, test_source)
    print(f"\nSource: {test_source}, Temperature: {test_temp}")
    print("Results:")
    for scale, value in results.items():
        print(f"{scale}: {value:.2f}")
    test_temp = 300.15
    test_source = "Kelvin"
    results = convert_temp(test_temp, test_source)
    print(f"\nSource: {test_source}, Temperature: {test_temp}")
    print("Results:")
    for scale, value in results.items():
        print(f"{scale}: {value:.2f}")