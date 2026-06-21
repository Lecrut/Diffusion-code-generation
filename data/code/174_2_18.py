def list_to_dict(pairs):
    result = {}
    for key, value in pairs:
        result[key] = value
    return result

if __name__ == '__main__':
    sample_pairs = [('name', 'Alice'), ('age', 30), ('name', 'Bob'), ('age', 25)]
    print(list_to_dict(sample_pairs))