def calculate_average_temperature(temperatures):
    """
    Calculates the arithmetic mean of a list of temperature readings.
    
    Args:
        temperatures (list[float]): A list containing float values representing 
                                   individual temperature measurements.
        
    Returns:
        float: The average temperature as a floating-point number.
               Returns None if the input list is empty to avoid division by zero errors,
               though typically an arithmetic mean requires at least one element.

    Raises:
        TypeError: If temperatures is not a list or contains non-numeric elements.
    
    Note: 
        Uses sum() and len() for efficiency as they are implemented in C.
    """
    if not isinstance(temperatures, list):
        raise TypeError("Input must be a list.")

    if any(not isinstance(temp, (int, float)) for temp in temperatures):
        raise ValueError("All elements in the temperature list must be numeric floats or ints.")

    return sum(temperatures) / len(temperatures)

if __name__ == '__main__':
    # Hard-coded sample values representing daily high temperatures over a week.
    readings = [72.5, 68.0, 71.3, 69.5, 74.2, 70.8, 67.9]

    average_temp = calculate_average_temperature(readings)

    print(f"The calculated average temperature is: {average_temp:.2f}")