import math
def convert_temp(temp, source_scale):
    results = {}
    if source_scale == "Celsius":
        results["Fahrenheit"] = (temp * 9/5) + 32
        results["Kelvin"] = temp + 273.15
    elif source_scale == "Fahrenheit":
        results["Celsius"] = (temp - 32) * 5/9
        results["Kelvin"] = (temp - 32) * 5/9 + 273.15
    elif source_scale == "Kelvin":
        results["Celsius"] = temp - 273.15
        results["Fahrenheit"] = (temp - 273.15) * 9/5 + 32
    else:
        raise ValueError("Unsupported source scale")
    return results
if __name__ == '__main__':
    test_cases = [
        (20, "Celsius"),
        (32, "Fahrenheit"),
        (273.15, "Kelvin"),
        (0, "Celsius"),
        (68, "Fahrenheit"),
        (300, "Kelvin")
    ]
    for temp, source in test_cases:
        try:
            conversions = convert_temp(temp, source)
            print(f"Source: {source}, Temp: {temp}")
            for target, converted_temp in conversions.items():
                print(f"{target}: {converted_temp:.2f}")
            print("-" * 20)
        except ValueError as e:
            print(f"Error for temp={temp}, source={source}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred for temp={temp}, source={source}: {e}")