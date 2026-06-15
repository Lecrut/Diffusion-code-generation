def find_matching_pairs(d1, d2):
    keys1 = set(d1.keys())
    keys2 = set(d2.keys())
    common_keys = keys1.intersection(keys2)
    matching_pairs = []
    for key in common_keys:
        if key in d1 and key in d2:
            matching_pairs.append((key, d1[key], d2[key]))
    return matching_pairs
if __name__ == '__main__':
    d1 = {
        'a': 10,
        'b': 20,
        'c': 30,
        'd': 40
    }
    d2 = {
        'c': 30,
        'd': 40,
        'e': 50,
        'f': 60
    }
    result = find_matching_pairs(d1, d2)
    print(result)