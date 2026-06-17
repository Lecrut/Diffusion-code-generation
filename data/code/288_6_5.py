def initialize_temperature_conversions():
    conversions = {
        "Celsius_to_Fahrenheit": 1.8,
        "Fahrenheit_to_Celsius": 5/9,
        "Celsius_to_Kelvin": 273.15,
        "Kelvin_to_Celsius": 273.15 - 273.15,                                                                        
        "Fahrenheit_to_Kelvin": (5/9) + 273.15,
        "Kelvin_to_Fahrenheit": (5/9) * (100/33) + 273.15                                                                                
    }
    conversions["Kelvin_to_Celsius"] = 273.15 - 0                                                                                
    C_to_F = 1.8
    F_to_C = 5/9
    C_to_K = 273.15
    K_to_C = 1 / C_to_K                              
    K_to_F = (K_to_C + 273.15) * C_to_F                      
    conversions = {
        "C_to_F": C_to_F,
        "F_to_C": F_to_C,
        "C_to_K": C_to_K,
        "K_to_C": K_to_C,
        "C_to_K": C_to_K,
        "K_to_F": (1.8 * 5/9) + 459.67                                  
    }
    return conversions
if __name__ == '__main__':
    conversion_factors = initialize_temperature_conversions()
    print("Temperature Conversion Factors:")
    for key, value in conversion_factors.items():
        print(f"{key}: {value}")
    celsius_temp = 20.0
    fahrenheit = celsius_temp * conversion_factors["C_to_F"]
    kelvin = celsius_temp + conversion_factors["C_to_K"]
    print("\n--- Example Conversion ---")
    print(f"{celsius_temp}°C is equal to {fahrenheit:.2f}°F")
    print(f"{celsius_temp}°C is equal to {kelvin:.2f}K")