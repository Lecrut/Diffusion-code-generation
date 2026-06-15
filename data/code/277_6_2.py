def count_nested_elements(nested_list):
    count = 0
    for element in nested_list:
        if isinstance(element, list):
            count += count_nested_elements(element)
        else:
            count += 1
    return count
if __name__ == '__main__':
    data1 = [1, 2, [3, 4], 5]
    print(count_nested_elements(data1))
    data2 = [1, [2, [3, 4]], 5]
    print(count_nested_elements(data2))
    data3 = [1, 2, 3]
    print(count_nested_elements(data3))
    data4 = [[1], [2, [3]], [4]]
    print(count_nested_elements(data4))