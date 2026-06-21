def unique_items(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

if __name__ == '__main__':
    sample_items = ['apple', 'banana', 'cherry', 'date', 'apple']
    unique_sample_items = unique_items(sample_items)
    print(unique_sample_items)