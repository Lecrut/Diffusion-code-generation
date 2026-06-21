def find_common_elements(list1, list2, tolerance):
    return [x for x in list1 if any(abs(x - y) <= tolerance for y in list2)]

if __name__ == '__main__':
    list1 = [0.1 + 0.2, 0.3, 0.4]
    list2 = [0.300001, 0.5, 0.6]
    tolerance = 1e-5
    print(find_common_elements(list1, list2, tolerance))