def convert_pairs_to_dict(pairs):
    result = {}
    for key, value in pairs:
        result[key] = value
    return result

if __name__ == '__main__':
    sample_pairs = [("Alice", 30), ("Bob", 25), ("Charlie", 35), ("Bob", 40)]
    final_dict = convert_pairs_to_dict(sample_pairs)
    print(final_dict)