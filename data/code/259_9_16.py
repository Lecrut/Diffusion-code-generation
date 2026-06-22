def find_min_max(dictionary):
    if not dictionary:
        return None, None
    min_value = max_value = next(iter(dictionary.values()))
    for value in dictionary.values():
        if value < min_value:
            min_value = value
        elif value > max_value:
            max_value = value
    return min_value, max_value

if __name__ == '__main__':
    sample_dict = {1: 3, 2: 5, 3: 1, 4: 8}
    print(find_min_max(sample_dict))