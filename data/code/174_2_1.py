def list_to_dict(pairs):
    result = {}
    for key, value in pairs:
        result[key] = value
    return result

if __name__ == '__main__':
    sample_pairs = [('a', 1), ('b', 2), ('a', 3)]
    print(list_to_dict(sample_pairs))