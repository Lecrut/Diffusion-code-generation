import statistics

def find_min_max_temperatures(temperatures):
    """
    Finds and returns the maximum and minimum temperatures from a list.
    
    Args:
        temperatures (list of float or int): List of temperature readings.
        
    Returns:
        tuple: A tuple containing (min_temp, max_temp).
            
    Raises:
        ValueError: If the input list is empty.
    """
    if not temperatures:
        raise ValueError("Input list cannot be empty.")

    min_value = float('inf')
    max_value = float('-inf')

    for temp in temperatures:
        if isinstance(temp, (int, float)) and isinstance(temp, numbers.Real):
            if temp < min_value:
                min_value = temp
            elif temp > max_value:
                max_value = temp
        else:
            raise TypeError(f"Unsupported temperature type: {type(temp)}")

    return min_value, max_value

if __name__ == '__main__':
    sample_data = [23.5, 18.0, 27.2, 19.5, 24.0]
    
    # Ensure all elements are numeric for safety in this context
    def ensure_numeric(item):
        if isinstance(item, (int, float)):
            return item
        try:
            return float(item)
        except (TypeError, ValueError):
            raise TypeError(f"Cannot convert {item} to a number.")

    validated_data = [ensure_numeric(t) for t in sample_data]
    
    min_temp, max_temp = find_min_max_temperatures(validated_data)
    print(f"Minimum temperature: {min_temp}")
    print(f"Maximum temperature: {max_temp}")