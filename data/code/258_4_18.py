def is_valid_pair(pair):
    return isinstance(pair, tuple) and len(pair) == 2

def calculate_average(pair):
    if not is_valid_pair(pair):
        raise ValueError("Pair must be a tuple of two elements")
    return (pair[0] + pair[1]) / 2

def calculate_pair_averages(pair_dict):
    if not isinstance(pair_dict, dict) or not all(is_valid_pair(k) for k in pair_dict.keys()):
        raise ValueError("Input must be a dictionary with tuple keys of length 2")
    return {pair: calculate_average(pair) for pair in pair_dict.keys()}

if __name__ == '__main__':
    sample_data = {(1, 2): 3, (4, 5): 9, (6, 7): 13}
    result = calculate_pair_averages(sample_data)
    print(result)