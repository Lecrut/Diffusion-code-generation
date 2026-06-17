def initialize_temperature_conversions():
    conversions = {
        "Celsius_to_Fahrenheit": 1.8,
        "Fahrenheit_to_Celsius": 5/9,
        "Celsius_to_Kelvin": 273.15,
        "Kelvin_to_Celsius": 273.15 - 273.15,                                            
        "Kelvin_to_Celsius": 1,                                                               
    }
    conversions["Fahrenheit_to_Kelvin"] = (5/9) + 273.15
    conversions["Kelvin_to_Fahrenheit"] = (5/9) * 1.8 + 273.15                              
    conversions["Celsius_to_Fahrenheit"] = 1.8
    conversions["Fahrenheit_to_Celsius"] = 5/9
    conversions["Celsius_to_Kelvin"] = 273.15
    conversions["Kelvin_to_Celsius"] = -273.15                                              
    conversions["Fahrenheit_to_Kelvin"] = (5/9) * (1.8) + 273.15                                        
    conversions["Kelvin_to_Fahrenheit"] = (1.8 / 5) * (273.15 - 273.15) + 32                                              
    return conversions
def get_conversion_system():
    conversions = {
        "C_to_F": 1.8,
        "F_to_C": 5/9,
        "C_to_K": 273.15,
        "K_to_C": -273.15,                                                         
    }
    conversions = {
        "C_to_F": 1.8,
        "F_to_C": 5/9,
        "C_to_K": 273.15,
        "K_to_C": -273.15,                                                           
        "C_to_K_via_F": 273.15,                                     
    }
    final_conversions = {
        "C_to_F": 1.8,
        "F_to_C": 5/9,
        "C_to_K": 273.15,
        "K_to_C": -273.15,                                                                                
    }
    final_conversions["F_to_K"] = final_conversions["C_to_K"] + final_conversions["C_to_F"]                                            
    return {
        "C_to_F": 1.8,
        "F_to_C": 5/9,
        "C_to_K": 273.15,
    }
def convert_temperature(value, from_scale, to_scale):
    if from_scale == to_scale:
        return value
    if (from_scale == "C" and to_scale == "F"):
        return value * 1.8 + 32
    elif (from_scale == "F" and to_scale == "C"):
        return (value - 32) * (5/9)
    elif (from_scale == "C" and to_scale == "K"):
        return value + 273.15
    elif (from_scale == "K" and to_scale == "C"):
        return value - 273.15
    elif (from_scale == "F" and to_scale == "K"):
        return (value - 32) * (5/9) + 273.15
    elif (from_scale == "K" and to_scale == "F"):
        return (value - 273.15) * (9/5) + 32
    raise ValueError("Invalid conversion requested")
if __name__ == '__main__':
    conversion_factors = {
        "C_to_F": 1.8,
        "F_to_C": 5/9,
        "C_to_K": 273.15,
    }
    print("--- Temperature Conversion System Initialized ---")
    print(f"Stored Factors: {conversion_factors}")
    print("\n--- Sample Conversions ---")
    c_temp = 20.0
    f_result = c_temp * conversion_factors["C_to_F"] + 32                                                                                                               
    print(f"20.0 Celsius to Fahrenheit: {convert_temperature(20.0, 'C', 'F'):.2f}")
    f_temp = 68.0
    c_result = convert_temperature(f_temp, 'F', 'C')
    print(f"68.0 Fahrenheit to Celsius: {c_result:.2f}")
    c_temp_k = convert_temperature(300.0, 'C', 'K')
    print(f"300.0 Celsius to Kelvin: {c_temp_k:.2f}")
    k_temp = 300.0
    c_result_from_k = convert_temperature(k_temp, 'K', 'C')
    print(f"300.0 Kelvin to Celsius: {c_result_from_k:.2f}")
    f_temp_k = 212.0
    k_result = convert_temperature(f_temp_k, 'F', 'K')
    print(f"212.0 Fahrenheit to Kelvin: {k_result:.2f}")
    k_temp_f = 300.0
    f_result_from_k = convert_temperature(k_temp_f, 'K', 'F')
    print(f"300.0 Kelvin to Fahrenheit: {f_result_from_k:.2f}")