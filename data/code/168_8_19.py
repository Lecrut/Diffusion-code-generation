from collections import defaultdict

def group_by_string_length(items):
    groups = defaultdict(list)
    for item in items:
        length = len(str(item))
        groups[length].append(item)
    return dict(groups)

if __name__ == '__main__':
    sample_items = [123, "hello", 456789, "world", 0.123]
    result = group_by_string_length(sample_items)
    print(result)