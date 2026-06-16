def initialize_temperature_conversions():
    conversions = {
        "Celsius_to_Fahrenheit": 1.8,
        "Fahrenheit_to_Celsius": 5/9,
        "Celsius_to_Kelvin": 273.15,
        "Kelvin_to_Celsius": 273.15 - 273.15,                                                      
        "Fahrenheit_to_Kelvin": (5/9) + 273.15,
        "Kelvin_to_Fahrenheit": (5/9) * (100/333.3333333333333)                     
    }
    conversions["Celsius_to_Kelvin"] = 273.15
    conversions["Kelvin_to_Celsius"] = 1 / 273.15
    return conversions
if __name__ == '__main__':
    temp_factors = initialize_temperature_conversions()
    print("Temperature Conversion Factors:")
    for key, value in temp_factors.items():
        print(f"{key}: {value}")
    celsius_temp = 20.0
    f_result = celsius_temp * temp_factors["Celsius_to_Fahrenheit"]
    k_result = celsius_temp + temp_factors["Celsius_to_Kelvin"]
    print("\n--- Example Conversion ---")
    print(f"{celsius_temp}°C is equal to {f_result:.2f}°F")
    print(f"{celsius_temp}°C is equal to {k_result:.2f}K")