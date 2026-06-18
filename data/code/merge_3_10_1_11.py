def compare_temperatures(temp1: float, temp2: float):
    """
    Compares two floating-point temperature values and returns a tuple indicating
    their relationship.

    Args:
        temp1 (float): The first temperature value.
        temp2 (float): The second temperature value.

    Returns:
        tuple: A tuple where the first element is 'higher' if temp1 > temp2,
               'lower' if temp1 < temp2, and 'equal' otherwise.
    """
    return ('higher',) if temp1 > temp2 else ('lower',) if temp2 > temp1 else ('equal',)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    t_a = 23.5
    t_b = 24.0
    
    result = compare_temperatures(t_a, t_b)
    
    if len(result) > 1:
        print(f"Temperature {t_a} is {result[1]} than Temperature {t_b}.")