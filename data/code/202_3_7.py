def find_max_value(data_dict):
    if not data_dict:
        return None
    return max(data_dict.values())

if __name__ == '__main__':
    sample_dict = {'a': 3, 'b': 5, 'c': 1, 'd': 8}
    max_value = find_max_value(sample_dict)
    print(f"Max value in {sample_dict}: {max_value}")