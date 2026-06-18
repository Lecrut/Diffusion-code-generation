def weight_difference_generator(pairs):
    """
    Generator function that yields the absolute difference between weights in each pair.
    
    Args:
        pairs (list of tuple or list): A list where each element is a sequence 
                                      containing two numeric values representing weights.
        
    Yields:
        float: The absolute difference between the two weights in each pair.
        
    Example:
        >>> gen = weight_difference_generator([(10, 5), (20, 30)])
        >>> list(gen)
        [5.0, 10.0]
    """
    for a, b in pairs:
        yield abs(a - b)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or files needed)
    weight_pairs = [(15.5, 20.3), (100, 98.7), (5.0, 5.0)]

    print("Weight differences:")
    for diff in weight_difference_generator(weight_pairs):
        print(f"{diff:.2f}")