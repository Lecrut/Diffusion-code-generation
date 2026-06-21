def group_by_length(items):
    groups = {}
    for item in items:
        length = len(str(item))
        if length not in groups:
            groups[length] = []
        groups[length].append(item)
    return groups

if __name__ == '__main__':
    sample_items = [123, "hello", 456789, "world", 0.12345]
    print(group_by_length(sample_items))