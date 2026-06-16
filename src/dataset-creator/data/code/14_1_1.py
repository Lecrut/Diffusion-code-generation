def filter_unique_elements(data):
    seen = set()
    result = []
    for item in data:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
if __name__ == '__main__':
    sample_list = [1, 2, 'apple', 3.5, 'banana', 1, 'cherry', None]
    unique_elements = filter_unique_elements(sample_list)
    print(unique_elements)