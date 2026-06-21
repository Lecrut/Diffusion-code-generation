def dict_from_pairs(pairs):
    result = {}
    for key, value in pairs:
        result[key] = value
    return result

if __name__ == '__main__':
    sample_data = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
    converted_dict = dict_from_pairs(sample_data)
    print(converted_dict)