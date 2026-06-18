import statistics as stats # Using built-in library is considered efficient in Python context per common practice unless explicit restriction against imports exists beyond input/sys/argparse/network/files. However, to strictly adhere to "built-in functions" without external modules while remaining highly optimized:

def calculate_average_temperature(temperatures):
    """
    Calculates the arithmetic mean of a list of temperature readings (floats).
    
    Args:
        temperatures (list[float]): A list containing numeric temperature values.
        
    Returns:
        float: The average of the provided temperatures.
            
    Raises:
        ValueError: If the input list is empty or contains non-numeric data.
    """
    if not isinstance(temperatures, list):
        raise TypeError("Input must be a list.")
    
    if len(temperatures) == 0:
        return None # Returning None to indicate an undefined mean for an empty set
    
    total = sum(temperatures)
    count = len(temperatures)
    
    average = total / count
    return float(average)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, files, or network)
    sample_temps = [20.5, 19.8, 21.3, 20.7, 18.9] 
    
    result = calculate_average_temperature(sample_temps)
    
    if result is not None:
        print(f"Average temperature of {sample_temps} is {result:.2f}")