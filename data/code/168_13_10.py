def group_by_length(items):
    length_dict = {}
    for item in items:
        length = len(item)
        if length not in length_dict:
            length_dict[length] = []
        length_dict[length].append(item)
    return {k: sorted(v) for k, v in length_dict.items()}

if __name__ == '__main__':
    sample_items = ["apple", "banana", "pear", "kiwi", "orange", "grape", "peach"]
    result = group_by_length(sample_items)
    print(result)