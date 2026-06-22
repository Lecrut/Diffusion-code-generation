def find_min_max(dictionary):
    if not dictionary:
        return None, None
    min_val = max_val = next(iter(dictionary.values()))
    for value in dictionary.values():
        if value < min_val:
            min_val = value
        elif value > max_val:
            max_val = value
    return min_val, max_val

if __name__ == '__main__':
    sample_dict = {'apple': 50, 'banana': 30, 'cherry': 20, 'date': 80}
    min_value, max_value = find_min_max(sample_dict)
    print(f"Minimum value: {min_value}, Maximum value: {max_value}")