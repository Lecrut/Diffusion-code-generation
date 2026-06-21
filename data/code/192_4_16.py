def are_close(value1, value2, tolerance=1e-9):
    return abs(value1 - value2) < tolerance

def find_common_elements(list_a, list_b, tolerance=1e-9):
    return [x for x in list_a if any(are_close(x, y, tolerance) for y in list_b)]

if __name__ == '__main__':
    list_a = [0.1 + 0.2, 0.3, 0.4]
    list_b = [0.3000000001, 0.5, 0.6]
    common_elements = find_common_elements(list_a, list_b)
    print(common_elements)