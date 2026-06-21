def find_common_elements(list_x, list_y):
    set_x = set(list_x)
    common = set_x.intersection(set(list_y))
    return list(common)

if __name__ == '__main__':
    list_a = [10, 20, 30, 40, 50]
    list_b = [40, 50, 60, 70, 80]
    common_elements = find_common_elements(list_a, list_b)
    print(f"Common elements: {common_elements}")