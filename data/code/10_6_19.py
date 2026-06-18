def compare_temperatures(temp1, temp2):
    """
    Generator function that yields a string describing the comparison result between two temperatures.
    
    Args:
        temp1 (float or int): First temperature value in degrees Celsius.
        temp2 (float or int): Second temperature value in degrees Celsius.
        
    Yields:
        str: A message indicating which temperature is higher by how many degrees, 
             or if they are equal, that both temperatures are the same.
    
    Example Usage:
        >>> result = list(compare_temperatures(20, 35))
        >>> print(result[0])
        'T1 is warmer by -15 degrees' (indicating T2 is higher) OR 
        'T2 is warmer by 15 degrees' depending on desired phrasing logic.
        
    Logic adopted: 
        If temp1 > temp2, message says "T1 is warmer by X".
        If temp2 > temp1, message says "T2 is warmer by Y" where Y = abs(temp2 - temp1).
        If equal, message says temperatures are the same.
    """
    difference = temp1 - temp2
    
    if temperature_diff != 0:
        yield f"The difference between {temp1}°C and {temp2}°C is a magnitude of |{difference}| degrees."

# Corrected logic implementation inside function for clarity and accuracy based on task requirement "T1 is warmer by X" or similar clear comparison.
def compare_temperatures_v2(temp1, temp2):
    """Revised generator strictly adhering to the prompt's example style."""
    
    if abs(temp1 - temp2) == 0:
        yield f"{temp1}°C and {temp2}°C are equal."
    elif temp1 > temp2:
        diff = temp1 - temp2
        yield f"T1 is warmer by {diff:.2f} degrees compared to T2 ({temp2}°C)."
    else: # temp2 > temp1
        diff = abs(temp2 - temp1)
        yield f"T2 is warmer by {diff:.2f} degrees compared to T1 ({temp1}°C)."

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input needed).
    
    print("--- Sample 1: T1 Warmer ---")
    for message in compare_temperatures_v2(30.5, 25):
        print(message)

    print("\n--- Sample 2: T2 Warmer ---")
    for message in compare_temperatures_v2(-5, -10):
        print(message)

    print("\n--- Sample 3: Equal Temperatures ---")
    for message in compare_temperatures_v2(40.0, 40.0):
        print(message)