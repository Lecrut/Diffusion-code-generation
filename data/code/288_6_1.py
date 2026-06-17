def initialize_temperature_conversions():
    conversions = {
        "Celsius_to_Fahrenheit": 1.8,
        "Fahrenheit_to_Celsius": 5/9,
        "Celsius_to_Kelvin": 273.15,
        "Kelvin_to_Celsius": 273.15 - 273.15,                                                                                      
        "Fahrenheit_to_Kelvin": (5/9) + 273.15,
        "Kelvin_to_Fahrenheit": (T - 273.15) * 9/5 + 32                                                                              
    }
    conversions_simplified = {
        "C_to_F": 1.8,
        "F_to_C": 5/9,
        "C_to_K": 273.15,
        "K_to_C": 1/273.15,
    }
    return conversions_simplified
def convert_temperature(value, from_scale, to_scale):
    if from_scale == to_scale:
        return value
    conversions = {
        "C_to_F": 1.8,
        "F_to_C": 5/9,
        "C_to_K": 273.15,
        "K_to_C": 1/273.15,
    }
    if from_scale == "Celsius" and to_scale == "Fahrenheit":
        return value * conversions["C_to_F"]
    elif from_scale == "Fahrenheit" and to_scale == "Celsius":
        return value * conversions["F_to_C"]
    elif from_scale == "Celsius" and to_scale == "Kelvin":
        return value + conversions["C_to_K"]
    elif from_scale == "Kelvin" and to_scale == "Celsius":
        return value * conversions["K_to_C"]
    elif from_scale == "Fahrenheit" and to_scale == "Kelvin":
        celsius = value * conversions["F_to_C"]
        return celsius + conversions["C_to_K"]
    elif from_scale == "Kelvin" and to_scale == "Fahrenheit":
        celsius = value * conversions["K_to_C"]
        return celsius * 9/5 + 32
    else:
        raise ValueError("Invalid scale combination")
if __name__ == '__main__':
    temp_celsius = 20.0
    print(f"Starting Temperature: {temp_celsius}°C\n")
    temp_f = convert_temperature(temp_celsius, "Celsius", "Fahrenheit")
    print(f"{temp_celsius}°C is equal to {temp_f:.2f}°F")
    temp_k = convert_temperature(temp_celsius, "Celsius", "Kelvin")
    print(f"{temp_celsius}°C is equal to {temp_k:.2f}K")
    print("\n--- Testing Round Trip (Fahrenheit to Celsius) ---")
    temp_f_roundtrip = 68.0
    temp_c_roundtrip = convert_temperature(temp_f_roundtrip, "Fahrenheit", "Celsius")
    print(f"{temp_f_roundtrip}°F is equal to {temp_c_roundtrip:.2f}°C")
    print("\n--- Testing Round Trip (Kelvin to Fahrenheit) ---")
    temp_k_roundtrip = 300.0
    temp_f_from_k = convert_temperature(temp_k_roundtrip, "Kelvin", "Fahrenheit")
    print(f"{temp_k_roundtrip}K is equal to {temp_f_from_k:.2f}°F")