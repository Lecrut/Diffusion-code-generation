def filter_and_map_pairs(pairs):
    return {int(k): v for k, v in pairs if k.isdigit() and isinstance(v, str) and len(v.split()) == 1}

if __name__ == '__main__':
    sample_pairs = [('1', 'apple'), ('2', 'banana'), ('3.5', 'cherry'), ('4', 'date')]
    filtered_pairs = filter_and_map_pairs(sample_pairs)
    print(filtered_pairs)