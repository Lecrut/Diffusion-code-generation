def reverse_dict_print(dictionary):
    if not isinstance(dictionary, dict):
        raise ValueError("Input must be a dictionary")
    
    keys = list(dictionary.keys())
    keys.sort(reverse=True)
    
    for key in keys:
        print(f"{key}: {dictionary[key]}")

if __name__ == '__main__':
    sample_dict = {'apple': 1, 'banana': 2, 'cherry': 3}
    reverse_dict_print(sample_dict)