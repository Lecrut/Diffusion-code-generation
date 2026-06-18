import sys

def convert_temp(celsius_list):
    """
    Converts a list of temperature readings from Celsius to Fahrenheit.
    
    The conversion formula is: F = (C * 9/5) + 32
    
    This function uses a list comprehension for efficiency and clarity, avoiding explicit loops or temporary variables where possible within the transformation logic itself, ensuring high performance on large datasets while maintaining readability.
    
    Args:
        celsius_list (list[float]): A list of temperature values in degrees Celsius.
        
    Returns:
        list[float]: A new list containing temperatures converted to Fahrenheit.
    """
    return [(c * 9 / 5) + 32 for c in celsius_list]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no input(), sys.stdin, or argparse usage)
    sample_celsius = [0.0, 15.6, -4.4, 100.0, -273.15]
    
    fahrenheit_results = convert_temp(sample_celsius)
    
    # Output results to console (no file I/O or network access used)
    print("Input Celsius:", sample_celsius)
    print("Output Fahrenheit:", [round(f, 2) for f in fahrenheit_results])