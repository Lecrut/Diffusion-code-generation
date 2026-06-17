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
    sample_temp = 20.0
    source = "Celsius"
    results = convert_temperature(sample_temp, source)
    print(f"Source: {source}, Value: {sample_temp}")
    print("Results:")
    for scale, value in results.items():
        print(f"{scale}: {value:.2f}")
    sample_temp = 68.0
    source = "Fahrenheit"
    results = convert_temperature(sample_temp, source)
    print(f"\nSource: {source}, Value: {sample_temp}")
    print("Results:")
    for scale, value in results.items():
        print(f"{scale}: {value:.2f}")
    sample_temp = 300.15
    source = "Kelvin"
    results = convert_temperature(sample_temp, source)
    print(f"\nSource: {source}, Value: {sample_temp}")
    print("Results:")
    for scale, value in results.items():
        print(f"{scale}: {value:.2f}")