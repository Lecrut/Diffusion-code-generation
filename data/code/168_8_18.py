def group_by_length(items):
    length_dict = {}
    for item in items:
        key = len(str(item))
        if key not in length_dict:
            length_dict[key] = []
        length_dict[key].append(item)
    return length_dict

if __name__ == '__main__':
    sample_items = [123, "hello", 456789, "world", "a", 10]
    grouped_items = group_by_length(sample_items)
    print(grouped_items)