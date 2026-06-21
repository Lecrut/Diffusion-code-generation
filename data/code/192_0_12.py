def find_common_elements(list1, list2):
    common = set()
    result = []
    for item in list1:
        if item in list2 and item not in common:
            common.add(item)
            result.append(item)
    return result

if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5, 5]
    list_b = [4, 5, 6, 7, 8, 4]
    print(find_common_elements(list_a, list_b))