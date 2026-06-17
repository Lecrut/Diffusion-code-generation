def filter_items(items, criterion):
    passed_items = []
    for item in items:
        if len(item) > criterion:
            passed_items.append(item)
    return passed_items
if __name__ == '__main__':
    sample_list = ["apple", "banana", "kiwi", "grapefruit", "orange"]
    min_length = 5
    result = filter_items(sample_list, min_length)
    for item in result:
        print(item)