def print_large_values(dictionary):
    for key, value in dictionary.items():
        if value > 10:
            print(f"{key}: {value}")

if __name__ == '__main__':
    sample_dict = {
        'x': 7,
        'y': 20,
        'z': 9
    }
    print_large_values(sample_dict)