def filter_unique_elements(data):
    seen = set()
    unique_list = []
    for item in data:
        if id(item) not in seen:
            seen.add(id(item))
            unique_list.append(item)
    return unique_list
if __name__ == '__main__':
    sample_data = [1, 2.0, 'a', True, None, False]
    result = filter_unique_elements(sample_data)
    print(result)