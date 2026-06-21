def validate_pairs(pairs):
    if not all(isinstance(pair, tuple) and len(pair) == 2 for pair in pairs):
        raise ValueError("All elements in the list must be tuples of length 2")

def pairs_to_dict(pairs):
    result = {}
    for key, value in pairs:
        result[key] = value
    return result

if __name__ == '__main__':
    sample_pairs = [("Alice", 30), ("Bob", 25), ("Charlie", 35), ("Bob", 40)]
    validate_pairs(sample_pairs)
    result_dict = pairs_to_dict(sample_pairs)
    print(result_dict)