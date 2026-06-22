def calculate_pair_averages(pair_dict):
    if not isinstance(pair_dict, dict) or not all(isinstance(k, tuple) and len(k) == 2 for k in pair_dict.keys()):
        raise ValueError("Input must be a dictionary with tuple keys of length 2")
    averages = {}
    for pair, value in pair_dict.items():
        avg = (pair[0] + pair[1]) / 2
        averages[pair] = avg
    return averages

if __name__ == '__main__':
    sample_data = {(1, 3): 4, (5, 7): 6, (9, 11): 10}
    result = calculate_pair_averages(sample_data)
    print(result)