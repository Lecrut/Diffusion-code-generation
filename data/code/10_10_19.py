def calculate_mean(temp1: float, temp2: float) -> str:
    """Calculates the arithmetic mean of two temperature readings.
    
    Args:
        temp1 (float): The first temperature reading.
        temp2 (float): The second temperature reading.
        
    Returns:
        str: The calculated mean formatted to two decimal places.
    """
    result = (temp1 + temp2) / 2
    return f"{result:.2f}"

if __name__ == '__main__':
    # Hard-coded sample values as per requirements
    t_value_1 = 23.56789
    t_value_2 = 24.01234
    
    mean_temperature = calculate_mean(t_value_1, t_value_2)
    
    print(mean_temperature)