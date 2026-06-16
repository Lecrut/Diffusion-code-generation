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
    test_temp = 20
    test_scales = ["Celsius", "Fahrenheit", "Kelvin"]
    for scale in test_scales:
        try:
            results = convert_temp(test_temp, scale)
            print(f"Source: {scale}, Temperature: {test_temp}")
            for target_scale, converted_temp in results.items():
                print(f"  -> {target_scale}: {converted_temp:.2f}")
            print("-" * 20)
        except ValueError as e:
            print(f"Error for source {scale}: {e}")