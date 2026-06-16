import math
def convert_temp(temp, source_scale):
    results = {}
    if source_scale == "Celsius":
        celsius = temp
        results["Celsius"] = celsius
        results["Fahrenheit"] = (celsius * 9/5) + 32
        results["Kelvin"] = celsius + 273.15
    elif source_scale == "Fahrenheit":
        fahrenheit = temp
        results["Fahrenheit"] = fahrenheit
        results["Celsius"] = (fahrenheit - 32) * 5/9
        results["Kelvin"] = (fahrenheit - 32) * 5/9 + 273.15
    elif source_scale == "Kelvin":
        kelvin = temp
        results["Kelvin"] = kelvin
        results["Celsius"] = kelvin - 273.15
        results["Fahrenheit"] = (kelvin - 273.15) * 9/5 + 32
    else:
        raise ValueError("Unsupported source scale")
    return results
if __name__ == '__main__':
    test_temp = 20
    print(f"Converting {test_temp}°C:")
    celsius_results = convert_temp(test_temp, "Celsius")
    for scale, value in celsius_results.items():
        print(f"{scale}: {value:.2f}")
    print("\nConverting 68°F:")
    fahrenheit_results = convert_temp(68, "Fahrenheit")
    for scale, value in fahrenheit_results.items():
        print(f"{scale}: {value:.2f}")
    print("\nConverting 300.15 K:")
    kelvin_results = convert_temp(300.15, "Kelvin")
    for scale, value in kelvin_results.items():
        print(f"{scale}: {value:.2f}")