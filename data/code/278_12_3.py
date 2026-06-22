def print_dict_pairs(dictionary):
    for key, value in dictionary.items():
        print(f"Key: {key}, Value: {value}")

if __name__ == '__main__':
    sample_dict = {'x': 10, 'y': 20, 'z': 30}
    print_dict_pairs(sample_dict)