from collections import defaultdict

def group_by_length(items):
    groups = defaultdict(list)
    for item in items:
        length = len(str(item))
        groups[length].append(item)
    return dict(groups)

if __name__ == '__main__':
    sample_items = [1, 'hello', 3.14, 'world', [], {}, 'a', 'abc']
    grouped_items = group_by_length(sample_items)
    print(grouped_items)