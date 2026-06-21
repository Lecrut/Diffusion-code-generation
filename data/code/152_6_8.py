def find_common_elements(list_x, list_y):
    set_x = set(list_x)
    common = []
    for item in list_y:
        if item in set_x and item not in common:
            common.append(item)
    return common

if __name__ == '__main__':
    list_x = [1, 2, 3, 4, 5]
    list_y = [4, 5, 6, 7, 8]
    common_elements = find_common_elements(list_x, list_y)
    print(f"Common elements found: {common_elements}")