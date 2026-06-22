def reverse_dict_by_key(input_dict):
    if not isinstance(input_dict, dict) or len(input_dict) == 0:
        raise ValueError("Input must be a non-empty dictionary")
    
    for key in sorted(input_dict.keys(), reverse=True):
        print(f"{key}: {input_dict[key]}")

if __name__ == '__main__':
    sample_dict = {'apple': 1, 'banana': 2, 'cherry': 3}
    reverse_dict_by_key(sample_dict)