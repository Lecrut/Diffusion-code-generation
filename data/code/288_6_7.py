def initialize_temperature_conversions():
    conversions = {
        "Celsius_to_Fahrenheit": 1.8,
        "Fahrenheit_to_Celsius": 5/9,
        "Celsius_to_Kelvin": 273.15,
        "Kelvin_to_Celsius": 273.15 - 273.15,                                                                                                                                  
        "Fahrenheit_to_Kelvin": (5/9) + 273.15,
        "Kelvin_to_Fahrenheit": (5/9) * 1.8 + 273.15                                                               
    }
    conversions = {
        "C_to_F": 1.8,
        "F_to_C": 5/9,
        "C_to_K": 273.15,
        "K_to_C": 1/273.15,
    }
    return conversions
def convert_temperature(value, from_scale, to_scale):
    if from_scale == to_scale:
        return value
    if from_scale == "Celsius":
        celsius = value
    elif from_scale == "Fahrenheit":
        celsius = (value - 32) * (5/9)
    elif from_scale == "Kelvin":
        celsius = value - 273.15
    else:
        raise ValueError("Invalid source scale")
    if to_scale == "Celsius":
        return celsius
    elif to_scale == "Fahrenheit":
        return celsius * 9/5 + 32
    elif to_scale == "Kelvin":
        return celsius + 273.15
    else:
        raise ValueError("Invalid target scale")
if __name__ == '__main__':
    conversion_factors = initialize_temperature_conversions()
    print("--- Temperature Conversion System Initialized ---")
    print(f"Conversion Factors Dictionary: {conversion_factors}")
    print("\n--- Sample Conversions (Using the defined factors for direct scale changes) ---")
    celsius_temp = 25.0
    f_result = celsius_temp * conversion_factors["C_to_F"]
    print(f"{celsius_temp}°C is {f_result:.2f}°F")
    fahrenheit_temp = 68.0
    c_result = fahrenheit_temp * conversion_factors["F_to_C"]
    print(f"{fahrenheit_temp}°F is {c_result:.2f}°C")
    celsius_temp = 100.0
    k_result = celsius_temp * conversion_factors["C_to_K"]
    print(f"{celsius_temp}°C is {k_result:.2f}K")
    kelvin_temp = 300.15
    c_from_k = kelvin_temp * conversion_factors["K_to_C"]
    print(f"{kelvin_temp}K is {c_from_k:.2f}°C")
    fahrenheit_temp = 77.0
    c_intermediate = (fahrenheit_temp - 32) * (5/9)
    k_result = c_intermediate + 273.15
    print(f"{fahrenheit_temp}°F is {k_result:.2f}K")