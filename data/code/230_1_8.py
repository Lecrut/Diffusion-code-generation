def filter_dict(input_dict):
    return [(key, value) for key, value in input_dict.items() if value >= 0]

if __name__ == '__main__':
    sample_dict = {'x': -5, 'y': 10, 'z': 0, 'w': 3}
    filtered_result = filter_dict(sample_dict)
    print(filtered_result)