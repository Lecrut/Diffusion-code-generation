import sys

def convert_temp(celsius_list: list) -> list:
    """
    Converts a list of temperatures from Celsius to Fahrenheit using an optimized 
    list comprehension approach. The formula used is F = (C * 9/5) + 32.
    
    Args:
        celsius_list (list): A list of numeric values representing temperatures in Celsius.
        
    Returns:
        list: A new list containing the corresponding temperatures in Fahrenheit.
    """
    return [(c * 9 / 5) + 32 for c in celsius_list]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or files needed)
    sample_celsius = [0, 10, 20.5, -4, 36.7]
    
    result_fahrenheit = convert_temp(sample_celsius)
    
    print(f"Celsius to Fahrenheit Conversion")
    for i in range(len(sample_celsius)):
        c_val = sample_celsius[i]
        f_val = result_fahrenheit[i]
        print(f"{c_val}°C -> {f_val:.2f}°F")