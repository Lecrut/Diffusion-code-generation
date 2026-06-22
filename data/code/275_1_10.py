def filter_dict_by_value(dictionary):
    large_values = {key: value for key, value in dictionary.items() if value > 10}
    return large_values

def print_large_values(large_values):
    for key, value in large_values.items():
        print(f"{key}: {value}")

if __name__ == '__main__':
    sample_dict = {
        'a': 5,
        'b': 12,
        'c': 8,
        'd': 15
    }
    
    large_values = filter_dict_by_value(sample_dict)
    print_large_values(large_values)