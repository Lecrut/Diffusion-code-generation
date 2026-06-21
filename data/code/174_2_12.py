def is_valid_pairs(pairs):
    return all(isinstance(pair, tuple) and len(pair) == 2 for pair in pairs)

def convert_pairs_to_dict(pairs):
    if not is_valid_pairs(pairs):
        raise ValueError("All elements in the list must be tuples of length 2")
    
    result = {}
    for key, value in pairs:
        result[key] = value
    return result

if __name__ == '__main__':
    sample_pairs = [("Alice", 30), ("Bob", 25), ("Charlie", 35), ("Bob", 40)]
    result_dict = convert_pairs_to_dict(sample_pairs)
    print(result_dict)