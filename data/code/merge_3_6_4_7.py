import itertools

def weight_difference_generator(weight_pairs):
    """
    Generator function that yields the absolute difference between weights in a list of pairs.
    
    Args:
        weight_pairs (list[tuple]): A list where each element is a tuple containing two numeric values representing weights.
        
    Yields:
        float: The absolute difference between the two weights in each pair.
    """
    if not isinstance(weight_pairs, list):
        raise TypeError("weight_pairs must be a list")
    
    for w1, w2 in weight_pairs:
        yield abs(w1 - w2)

if __name__ == '__main__':
    sample_data = [
        (50.0, 48.5),
        (120.3, 125.7),
        (10.0, 10.0),
        (99.99, 100.01)
    ]

    results = list(weight_difference_generator(sample_data))
    
    print("Weight differences:")
    for i, diff in enumerate(results):
        pair_info = f"Pair {i+1}: |{sample_data[i][0]} - {sample_data[i][1]}| = {diff}"
        print(pair_info)