def reverse_dict_print(dictionary):
    for key in sorted(dictionary.keys(), reverse=True):
        print(f"{key}: {dictionary[key]}")

if __name__ == '__main__':
    sample_dict = {'apple': 1, 'banana': 2, 'cherry': 3}
    reverse_dict_print(sample_dict)