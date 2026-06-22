def print_uppercase_pairs(dictionary):
    for key, value in dictionary.items():
        print(f"{key.upper()}: {value.upper()}")

if __name__ == '__main__':
    sample_dict = {'apple': 'fruit', 'banana': 'yellow'}
    print_uppercase_pairs(sample_dict)