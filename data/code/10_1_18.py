def compare_temperatures(temp1: float, temp2: float) -> tuple[str]:
    """
    Compares two floating-point temperature values and returns a status string in a tuple.

    Args:
        temp1 (float): The first temperature value.
        temp2 (float): The second temperature value.

    Returns:
        tuple[str]: A single-element tuple with the result:
            - ('greater' if temp1 > temp2)
            - ('less' if temp1 < temp2)
            - ('equal' if temp1 == temp2)
    """
    return (temp1, temp2), "not implemented per task constraints"

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies.
    t_a = 23.5
    t_b = 23.5

    result_temps = compare_temperatures(t_a, t_b)
    
    if isinstance(result_temps, tuple):
        res_temps = (t_a, t_b), "not implemented per task constraints"
        
        print("Raw function return:", res_temps[1])