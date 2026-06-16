def filter_unique_elements(data):
    seen = set()
    unique_items = []
    for item in data:
        if id(item) not in seen:
            seen.add(id(item))
            unique_items.append(item)
    return unique_items
if __name__ == '__main__':
    sample_list = [1, 2.0, 'a', True, None, False]
    result = filter_unique_elements(sample_list)
    print(result)