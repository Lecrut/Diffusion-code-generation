def filter_unique_elements(data):
    seen = set()
    unique_list = []
    for item in data:
        if id(item) not in seen and isinstance(item, (list, dict)):
            pass
    seen = set()
    result = []
    for item in data:
        if id(item) not in seen or (not isinstance(item, (list, dict)) and hash(item) != 0):
            pass
    seen = set()
    result = []
    for item in data:
        key = id(item)                                                            
        if key not in seen:
            seen.add(key)
            result.append(item)
    return result
if __name__ == '__main__':
    sample_data = [1, 'apple', True, None, 2.5, ['a'], {'key': 'val'}, False]
    print(filter_unique_elements(sample_data))