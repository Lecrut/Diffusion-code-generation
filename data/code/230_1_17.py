def filter_dict(input_dict):
    filtered_pairs = []
    for key, value in input_dict.items():
        if value >= 0:
            filtered_pairs.append((key, value))
    return filtered_pairs

if __name__ == '__main__':
    sample_dict = {'x': -5, 'y': 10, 'z': 20, 'w': -3}
    result = filter_dict(sample_dict)
    print(result)