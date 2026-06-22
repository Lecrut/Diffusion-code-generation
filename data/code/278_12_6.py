sample_dict = {
    'apple': 1,
    'banana': 2,
    'cherry': 3
}

def print_key_value_pairs(dictionary):
    for key, value in dictionary.items():
        print(f'Key: {key}, Value: {value}')

if __name__ == '__main__':
    print_key_value_pairs(sample_dict)