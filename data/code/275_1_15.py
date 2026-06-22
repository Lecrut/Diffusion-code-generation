sample_dict = {'a': 5, 'b': 12, 'c': 8, 'd': 15}

def print_large_values(dictionary):
    for key, value in dictionary.items():
        if value > 10:
            print(f"{key}: {value}")

if __name__ == '__main__':
    print_large_values(sample_dict)