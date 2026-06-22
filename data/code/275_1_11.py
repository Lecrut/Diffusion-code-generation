def filter_and_print_large_values(input_dict):
    for key, value in input_dict.items():
        if value > 10:
            print(f"{key}: {value}")

if __name__ == '__main__':
    sample_dict = {
        'x': 7,
        'y': 20,
        'z': 9,
        'w': 30
    }
    filter_and_print_large_values(sample_dict)