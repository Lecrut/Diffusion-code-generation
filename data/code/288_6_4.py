def setup_temperature_conversions():
    conversion_factors = {
        "Celsius_to_Fahrenheit": 9/5,
        "Fahrenheit_to_Celsius": 5/9,
        "Celsius_to_Kelvin": 273.15,
        "Kelvin_to_Celsius": 1/273.15,
        "Fahrenheit_to_Kelvin": 5/9 + 273.15,
        "Kelvin_to_Fahrenheit": (100/9) * (5/9) + 273.15                                         
    }
    return conversion_factors
if __name__ == '__main__':
    conversion_data = setup_temperature_conversions()
    print("Temperature Conversion Factors:")
    for key, factor in conversion_data.items():
        print(f"{key}: {factor}")
    celsius_temp = 25.0
    fahrenheit_temp = 77.0
    kelvin_temp = 298.15
    print("\nSample Conversions:")
    c_to_f = celsius_temp * conversion_data["Celsius_to_Fahrenheit"]
    print(f"{celsius_temp}°C is {c_to_f:.2f}°F")
    f_to_c = fahrenheit_temp * conversion_data["Fahrenheit_to_Celsius"]
    print(f"{fahrenheit_temp}°F is {f_to_c:.2f}°C")
    c_to_k = celsius_temp * conversion_data["Celsius_to_Kelvin"]
    print(f"{celsius_temp}°C is {c_to_k:.2f}K")
    k_to_c = kelvin_temp * conversion_data["Kelvin_to_Celsius"]
    print(f"{kelvin_temp}K is {k_to_c:.2f}°C")
    f_to_k = fahrenheit_temp * conversion_data["Fahrenheit_to_Kelvin"]
    print(f"{fahrenheit_temp}°F is {f_to_k:.2f}K")