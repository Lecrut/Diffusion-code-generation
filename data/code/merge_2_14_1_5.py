def filter_unique_elements(data):
    seen = set()
    result = []
    for item in data:
        if id(item) not in seen and isinstance(item, (list, dict)):
            try:
                key = tuple(sorted((type(item).__name__, str(item))))
            except TypeError:
                continue
            if item not in result:
                result.append(item)
    return result
if __name__ == '__main__':
    sample_data = [1, 2, 'apple', 3.5, 'banana', 4, (1, 2), {'a': 1}, 
                   [1], 'orange', {1: 2}, list((1, 2))]
    filtered_result = filter_unique_elements(sample_data)
    print(filtered_result)