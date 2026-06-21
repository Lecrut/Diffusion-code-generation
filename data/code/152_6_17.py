def find_common_elements(list_x, list_y):
    set_x = set(list_x)
    common = set_x.intersection(set(list_y))
    return list(common)

if __name__ == '__main__':
    LIST_X = list(range(1, 1000001))
    LIST_Y = list(range(500001, 1500001))
    common_elements = find_common_elements(LIST_X, LIST_Y)
    print(f"Number of common elements found: {len(common_elements)}")
    print(f"First 10 common elements: {common_elements[:10]}")