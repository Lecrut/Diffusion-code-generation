def find_min_max(dictionary):
    if not dictionary:
        return None, None
    min_value = min(dictionary.values())
    max_value = max(dictionary.values())
    return min_value, max_value

if __name__ == '__main__':
    sample_dict = {1: 34, 2: 78, 3: 56, 4: 23}
    min_val, max_val = find_min_max(sample_dict)
    print(f"Minimum value: {min_val}, Maximum value: {max_val}")