def find_last_greater_equal(data, threshold):
    n = len(data)
    result = -1
    for i in range(n - 1, -1, -1):
        if data[i] >= threshold:
            result = i
            break
    return result
if __name__ == '__main__':
    list1 = [10, 5, 20, 15, 8, 22, 1]
    threshold1 = 18
    print(find_last_greater_equal(list1, threshold1))
    list2 = [3, 7, 1, 5, 9, 2]
    threshold2 = 6
    print(find_last_greater_equal(list2, threshold2))
    list3 = [5, 5, 5, 5]
    threshold3 = 5
    print(find_last_greater_equal(list3, threshold3))
    list4 = [1, 2, 3, 4]
    threshold4 = 5
    print(find_last_greater_equal(list4, threshold4))
    list5 = [100, 200, 300]
    threshold5 = 50
    print(find_last_greater_equal(list5, threshold5))