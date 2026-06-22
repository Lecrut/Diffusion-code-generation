def print_uppercase_dict(dictionary):
    for key, value in dictionary.items():
        print(f"{key.upper()}: {value.upper()}")

if __name__ == '__main__':
    sample_dict = {'apple': 'fruit', 'banana': 'yellow'}
    print_uppercase_dict(sample_dict)