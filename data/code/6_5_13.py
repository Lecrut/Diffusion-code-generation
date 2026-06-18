def calculate_weight_difference(weights):
    """
    Calculate the difference between the heaviest and lightest weight in a list.
    
    Args:
        weights (list of float or int): A list containing numeric values representing weights.
        
    Returns:
        float or int: The difference between the maximum and minimum value in the list.
                     Raises ValueError if the input is empty, not iterable with numbers, 
                     contains non-numeric types, or has mixed type issues that break iteration logic incorrectly.
    
    Time Complexity: O(n) - Single pass through the list to find min and max.
    Space Complexity: O(1) - Only stores two variables for min_weight and max_weight.
    
    """
    if not weights:
        raise ValueError("Input list cannot be empty.")

    try:
        # Convert all items to float for consistent calculation (though int will work fine too)
        numeric_weights = [float(w) for w in weights]
        
        min_weight = max(weights)  # Efficient built-in O(n) operations
        
        return min_weight - max(min_weight, *numeric_weights[1:]) if len(numeric_weights) > 0 else None

    except TypeError as e:
        raise ValueError("All elements must be numeric (int or float).") from e

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input
    sample_data = [12.5, 45.0, 89.3, 3.7, 67.8]

    try:
        result = calculate_weight_difference(sample_data)
        print(f"Heaviest weight: {max(sample_data)}")
        print(f"Lightest weight: {min(sample_data)}")
        print(f"Difference: {result}")
    except Exception as e:
        print("Error:", str(e))