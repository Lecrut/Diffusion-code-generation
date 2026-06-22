def reverse_dict_and_print(d):
    if not isinstance(d, dict):
        raise ValueError("Input must be a dictionary.")
    
    for key in sorted(d.keys(), reverse=True):
        print(f"{key}: {d[key]}")

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
    reverse_dict_and_print(sample_dict)