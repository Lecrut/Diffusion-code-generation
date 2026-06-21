def find_common_elements(list_x, list_y):
    set_x = set(list_x)
    common = set()
    for item in list_y:
        if item in set_x and item not in common:
            common.add(item)
    return list(common)

if __name__ == '__main__':
    list_x = list(range(1, 1000001))
    list_y = list(range(500001, 1500001))
    common_elements = find_common_elements(list_x, list_y)
    print(f"Number of common elements found: {len(common_elements)}")
    print(f"First 10 common elements: {common_elements[:10]}")