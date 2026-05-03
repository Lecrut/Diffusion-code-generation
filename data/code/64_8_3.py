def find_last_greater_equal(data, threshold):
    n = len(data)
    result = -1
    for i in range(n - 1, -1, -1):
        if data[i] >= threshold:
            result = i
            break
    return result
if __name__ == '__main__':
    list1 = [10, 20, 30, 40, 50]
    threshold1 = 35
    print(find_last_greater_equal(list1, threshold1))
    list2 = [5, 15, 25, 35, 45]
    threshold2 = 30
    print(find_last_greater_equal(list2, threshold2))
    list3 = [1, 2, 3, 4, 5]
    threshold3 = 6
    print(find_last_greater_equal(list3, threshold3))
    list4 = [100, 50, 200, 150]
    threshold4 = 180
    print(find_last_greater_equal(list4, threshold4))
    list5 = [1, 1, 1, 1]
    threshold5 = 0
    print(find_last_greater_equal(list5, threshold5))