def find_common_elements(list_x, list_y):
    set_x = set(list_x)
    common = []
    for item in list_y:
        if item in set_x and item not in common:
            common.append(item)
    return common

if __name__ == '__main__':
    list_x = list(range(10000))
    list_y = list(range(5000, 15000))
    common_elements = find_common_elements(list_x, list_y)
    print(f"Number of common elements found: {len(common_elements)}")
    print(f"First 10 common elements: {common_elements[:10]}")