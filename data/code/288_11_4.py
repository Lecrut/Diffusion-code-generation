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
    sample_temp = 20.0
    source = "Celsius"
    results = convert_temperature(sample_temp, source)
    print(f"Source: {source}, Value: {sample_temp}")
    print(f"Results: {results}")
    sample_temp_f = 68.0
    source_f = "Fahrenheit"
    results_f = convert_temperature(sample_temp_f, source_f)
    print(f"\nSource: {source_f}, Value: {sample_temp_f}")
    print(f"Results: {results_f}")
    sample_temp_k = 300.15
    source_k = "Kelvin"
    results_k = convert_temperature(sample_temp_k, source_k)
    print(f"\nSource: {source_k}, Value: {sample_temp_k}")
    print(f"Results: {results_k}")