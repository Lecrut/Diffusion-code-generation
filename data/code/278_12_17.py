def print_dict_entries(dictionary):
    for key, value in dictionary.items():
        print(f"Key: {key}, Value: {value}")

if __name__ == '__main__':
    sample_data = {'apple': 3, 'banana': 5, 'cherry': 2}
    print_dict_entries(sample_data)