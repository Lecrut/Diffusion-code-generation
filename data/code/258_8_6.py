def validate_pairs(pairs):
    for pair in pairs:
        if not isinstance(pair, (list, tuple)) or len(pair) != 2 or not all(isinstance(x, (int, float)) for x in pair):
            raise ValueError("All pairs must contain exactly two numbers.")

def average_pairs(pairs):
    return tuple((a + b) / 2 for a, b in pairs)

if __name__ == '__main__':
    sample_data_valid = [
        [1, 2],
        [3, 4],
        [5, 6]
    ]
    
    validate_pairs(sample_data_valid)
    result = average_pairs(sample_data_valid)
    print(result)