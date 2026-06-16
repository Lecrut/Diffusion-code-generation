def filter_items(items, criterion):
    result = []
    for item in items:
        if len(item) > criterion:
            result.append(item)
    return result
if __name__ == '__main__':
    sample_list = ["apple", "banana", "kiwi", "strawberry", "grapefruit"]
    threshold = 5
    filtered_items = filter_items(sample_list, threshold)
    for item in filtered_items:
        print(item)