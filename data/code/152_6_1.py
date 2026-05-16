def find_common_elements(list_x, list_y):
    set_x = set(list_x)
    common = set_x.intersection(set(list_y))
    return list(common)
if __name__ == '__main__':
    list_x = list(range(1000000))
    list_y = list(range(500000, 1500000))
    common_elements = find_common_elements(list_x, list_y)
    print(common_elements)