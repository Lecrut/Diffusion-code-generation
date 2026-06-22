def uppercase_dict_values(input_dict):
    for key, value in input_dict.items():
        print(f"{key.upper()}: {value.upper()}")

if __name__ == '__main__':
    sample_dict = {'apple': 'red', 'banana': 'yellow', 'cherry': 'red'}
    uppercase_dict_values(sample_dict)