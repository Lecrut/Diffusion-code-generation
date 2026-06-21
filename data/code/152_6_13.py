def find_common_elements(list_x, list_y):
    set_x = set(list_x)
    common_elements = [item for item in list_y if item in set_x]
    return common_elements

if __name__ == '__main__':
    MAX_VALUE = 1500001
    MIN_VALUE = 500001
    list_x = range(1, MAX_VALUE)
    list_y = range(MIN_VALUE, MAX_VALUE)
    common_elements = find_common_elements(list_x, list_y)
    print(f"Number of common elements found: {len(common_elements)}")
    print(f"First 10 common elements: {common_elements[:10]}")