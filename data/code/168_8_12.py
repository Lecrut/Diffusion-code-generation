def group_by_length(items):
    from collections import defaultdict
    grouped = defaultdict(list)
    for item in items:
        length = len(str(item))
        grouped[length].append(item)
    return dict(grouped)

if __name__ == '__main__':
    sample_items = [1, 'hello', 3.14, 'world', [], {}, (1, 2), {'a': 1}]
    print(group_by_length(sample_items))