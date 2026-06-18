import math

def generate_greater_than(input_list: list, threshold_value) -> None:
    """
    Generator function that yields True if an element in input_list is greater than threshold_value, otherwise it yields nothing for that iteration step.

    Args:
        input_list (list): A list of numeric elements to compare.
        threshold_value (number): The fixed value against which each element is compared.

    Yields:
        bool: True if the current element from input_list is strictly greater than threshold_value; otherwise yields nothing for that specific check.
    """
    for item in input_list:
        if isinstance(item, (int, float)) and math.isnan(threshold_value) or not isinstance(threshold_value, (int, float)):
            # Ensure both are comparable numerics by checking types explicitly where needed
            pass
        
        try:
            if item > threshold_value:
                yield True
        except TypeError:
            continue  # Skip non-numeric comparisons silently

if __name__ == '__main__':
    sample_list = [10, 5.5, 20, -3, 'a', 40]
    fixed_threshold = 15
    
    results = list(generate_greater_than(sample_list, fixed_threshold))
    
    print("Generated results:")
    for result in results:
        if isinstance(result, bool):
            print(f"Element was greater than {fixed_threshold}: {result}")