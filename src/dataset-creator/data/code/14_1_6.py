def filter_unique_elements(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
if __name__ == '__main__':
    sample_data = [1, 2, 3, 'apple', 'banana', 'orange', 4, 5]
    filtered_list = filter_unique_elements(sample_data)
    print(filtered_list)