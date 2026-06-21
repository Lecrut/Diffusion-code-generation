def find_common_elements(list_x, list_y):
    common = []
    set_y = set(list_y)
    for item in list_x:
        if item in set_y and item not in common:
            common.append(item)
    return common

if __name__ == '__main__':
    list_x = list(range(1000000))
    list_y = list(range(500000, 1500000))
    common_elements = find_common_elements(list_x, list_y)
    print(f"Number of common elements found: {len(common_elements)}")
    print(f"First 10 common elements: {common_elements[:10]}")