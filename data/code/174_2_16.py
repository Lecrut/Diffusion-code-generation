def list_to_dict(pairs):
    return dict(pairs)

if __name__ == '__main__':
    sample_pairs = [('a', 1), ('b', 2), ('a', 3)]
    result = list_to_dict(sample_pairs)
    print(result)