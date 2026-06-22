def filter_and_print_dict(input_dict):
    for key, value in input_dict.items():
        if value > 10:
            print(f"{key}: {value}")

if __name__ == '__main__':
    sample_dict = {
        'a': 5,
        'b': 12,
        'c': 8,
        'd': 15
    }
    filter_and_print_dict(sample_dict)