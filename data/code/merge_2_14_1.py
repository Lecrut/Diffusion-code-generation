def filter_unique_elements(data):
    seen = {}
    unique_items = []
    for item in data:
        if item not in seen:
            seen[item] = True
            unique_items.append(item)
    return unique_items
if __name__ == '__main__':
    sample_data = [1, 2, 'apple', 3.5, 'banana', 4, 'orange', 3.5, 'apple']
    result = filter_unique_elements(sample_data)
    print(result)