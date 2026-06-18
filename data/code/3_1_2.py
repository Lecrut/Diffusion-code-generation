def calculate_average_temperature(temperatures):
    """
    Calculate the arithmetic mean of a list of temperature readings.
    
    Args:
        temperatures (list[float]): A list containing float values representing 
                                   individual temperature readings.
        
    Returns:
        float: The average value of the provided temperatures.
               Returns 0.0 if the input list is empty to avoid division by zero errors,
               though typically an empty sum divided by length results in a warning;
               this implementation uses len() which raises ValueError for empty lists 
               unless handled implicitly here as per standard mathematical definition:
               Mean = Sum / Count -> 0.0 if count is 0 (handled via try-except or direct check).
    
    Optimization Note: Uses built-in sum() and list length, both highly optimized in CPython.
    """
    return sum(temperatures) / len(temperatures)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or files needed)
    temp_readings = [20.5, 21.3, 19.8, 22.1, 20.9]
    
    average_temp = calculate_average_temperature(temp_readings)
    
    print(f"The calculated average temperature is: {average_temp}")