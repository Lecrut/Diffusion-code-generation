# Temperature Average Calculator Module
# This script calculates the average of two temperature values provided by the user,
# with robust error handling for non-numeric inputs. It does not use any interactive prompts,
# command-line arguments, or external dependencies beyond the standard library.

def calculate_average_temperature(temp1: float, temp2: float) -> float:
    """
    Calculates and returns the average of two temperature values.
    
    Parameters:
        temp1 (float): The first temperature value.
        temp2 (float): The second temperature value.
        
    Returns:
        float: The average of the two temperatures.
        
    Raises:
        TypeError: If either input is not a numeric type.
    """
    if not isinstance(temp1, (int, float)) or not isinstance(temp2, (int, float)):
        raise TypeError("Both inputs must be numeric values.")
    
    average = (temp1 + temp2) / 2
    return average

def get_temperature_input(prompt: str) -> tuple[float, float]:
    """
    Simulates the input process using predefined sample values.
    This function replaces user interaction to ensure the script runs without external inputs.
    
    Parameters:
        prompt (str): A placeholder string for future interactive use.
        
    Returns:
        tuple[float, float]: A tuple containing two numeric temperature values.
    """
    # Hard-coded sample values as per requirements
    return 25.0, -10.0

if __name__ == '__main__':
    try:
        temp_a = get_temperature_input("Enter first temperature (simulated)")
        temp_b = get_temperature_input("Enter second temperature (simulated)")

        average_temp = calculate_average_temperature(temp_a, temp_b)
        
        print(f"The average of {temp_a}°C and {temp_b}°C is {average_temp:.2f}°C.")
    except TypeError as e:
        print(f"Error: Invalid input type. {e}")
    except Exception as e:
        # Catch any unexpected errors to ensure robustness
        print(f"An unexpected error occurred: {e}")