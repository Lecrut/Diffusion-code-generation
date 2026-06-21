def merge_pairs_into_dict(pairs):
    result = {}
    for key, value in pairs:
        result[key] = value
    return result

if __name__ == '__main__':
    sample_pairs = [("Alice", 30), ("Bob", 25), ("Charlie", 35), ("Bob", 40)]
    merged_dict = merge_pairs_into_dict(sample_pairs)
    print(merged_dict)