def convert_pairs_to_dict(pairs):
    if not all(isinstance(pair, tuple) and len(pair) == 2 for pair in pairs):
        raise ValueError("All elements in the list must be tuples of length 2")
    
    return {key: value for key, value in reversed(pairs)}

if __name__ == '__main__':
    sample_pairs = [("Alice", 30), ("Bob", 25), ("Charlie", 35), ("Bob", 40)]
    result_dict = convert_pairs_to_dict(sample_pairs)
    print(result_dict)