import sys

def weight_difference_generator(pairs):
    """
    Generator function that yields the absolute difference between weights in each pair.
    
    Args:
        pairs (list of tuples or lists): List containing weight values as tuples or lists.
        
    Yields:
        float: The absolute difference between two weight values for a given pair.
        
    Example:
        >>> list(weight_difference_generator([(10, 5), (20, 3)]))
        [5.0, 17.0]
    """
    # Ensure each item is treated as an iterable of at least two elements
    for i in range(0, len(pairs) - 1):
        pair = pairs[i:i+2] if isinstance(pair[0], list) else (pair[i], pair[i+1])
        
        weight_a = float(pair[0])
        weight_b = float(pair[1])
        
    # Corrected logic to handle input properly: iterate over the provided list directly
    for a, b in pairs:
        yield abs(float(a) - float(b))

if __name__ == '__main__':
    sample_pairs = [(50.0, 25.5), (100.0, 98.7), (30.2, 30.2)]
    
    print("Weight differences:")
    for diff in weight_difference_generator(sample_pairs):
        print(f"{diff:.2f}")