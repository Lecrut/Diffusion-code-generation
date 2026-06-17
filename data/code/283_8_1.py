def filter_items(items, criterion):
    result = []
    for item in items:
        if len(item) > criterion:
            result.append(item)
    return result
if __name__ == '__main__':
    sample_list = ["apple", "banana", "kiwi", "grapefruit", "orange"]
    length_criterion = 5
    passing_items = filter_items(sample_list, length_criterion)
    for item in passing_items:
        print(item)