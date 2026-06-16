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
    test_scales = ["Celsius", "Fahrenheit", "Kelvin"]
    for scale in test_scales:
        try:
            results = convert_temperature(test_temp, scale)
            print(f"Source Scale: {scale}, Input Temperature: {test_temp}")
            for target_scale, value in results.items():
                print(f"  {target_scale}: {value:.2f}")
        except ValueError as e:
            print(f"Error for scale {scale}: {e}")
        print("-" * 20)
    test_temp_freezing = 0.0
    print("Testing Freezing Point (0 C):")
    results_c = convert_temperature(0.0, "Celsius")
    print(f"Source Scale: Celsius, Input Temperature: 0.0")
    for target_scale, value in results_c.items():
        print(f"  {target_scale}: {value:.2f}")
    print("-" * 20)
    test_temp_boiling = 100.0
    print("Testing Boiling Point (100 C):")
    results_f = convert_temperature(100.0, "Celsius")
    print(f"Source Scale: Celsius, Input Temperature: 100.0")
    for target_scale, value in results_f.items():
        print(f"  {target_scale}: {value:.2f}")
    print("-" * 20)
    test_temp_absolute_zero = 0.0
    print("Testing Absolute Zero (0 K):")
    results_k = convert_temperature(0.0, "Kelvin")
    print(f"Source Scale: Kelvin, Input Temperature: 0.0")
    for target_scale, value in results_k.items():
        print(f"  {target_scale}: {value:.2f}")
    print("-" * 20)