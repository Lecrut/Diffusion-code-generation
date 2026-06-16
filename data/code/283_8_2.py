def filter_items(items, criterion):
    result = []
    for item in items:
        if len(item) > criterion:
            result.append(item)
    return result
if __name__ == '__main__':
    sample_list = ["apple", "banana", "kiwi", "orange", "grapefruit"]
    min_length = 5
    filtered_items = filter_items(sample_list, min_length)
    for item in filtered_items:
        print(item)