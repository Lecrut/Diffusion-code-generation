def group_by_length(items):
    from collections import defaultdict
    groups = defaultdict(list)
    for item in items:
        length = len(str(item))
        groups[length].append(item)
    return dict(groups)

if __name__ == '__main__':
    sample_items = [123, 'hello', 456789, 'world', 0.12345]
    print(group_by_length(sample_items))