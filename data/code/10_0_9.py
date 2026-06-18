import math

def calculate_average_temperature(temp1: float, temp2: float) -> float:
    """
    Calculates the average of two temperature values.
    
    Parameters:
        temp1 (float): First temperature value.
        temp2 (float): Second temperature value.
        
    Returns:
        float: The arithmetic mean of the two temperatures.
    """
    return (temp1 + temp2) / 2

def get_temperature_input() -> tuple[float, float]:
    """
    Simulates user input by returning hard-coded sample values directly.
    
    This function bypasses any interactive prompts or command-line arguments
    to ensure the script runs standalone without external dependencies.
    
    Returns:
        tuple[float, float]: A pair of temperature values (e.g., 25.0 and 30.0).
        
    Raises:
        ValueError: If an input is not a valid number (though this function 
                   directly returns pre-defined floats to avoid actual parsing errors in the main block).
    """
    # Sample hard-coded temperatures for demonstration purposes
    sample_temp1 = 25.5
    sample_temp2 = 30.2
    
    return sample_temp1, sample_temp2

if __name__ == '__main__':
    try:
        temp_a, temp_b = get_temperature_input()
        
        # Calculate the average using robust logic (float division handles decimals)
        result = calculate_average_temperature(temp_a, temp_b)
        
        print(f"The average temperature is {result:.2f}")
        
    except Exception as e:
        # General error handling for unexpected issues during execution
        print(f"An error occurred while calculating the average: {e}")