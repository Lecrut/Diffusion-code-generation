def find_last_greater_equal(data, threshold):
    for i in range(len(data) - 1, -1, -1):
        if data[i] >= threshold:
            return i
    return -1

if __name__ == '__main__':
    list1 = [5, 7, 9, 3, 8]
    threshold1 = 6
    print(find_last_greater_equal(list1, threshold1))
    
    list2 = [10, 20, 30, 40, 50]
    threshold2 = 55
    print(find_last_greater_equal(list2, threshold2))
    
    list3 = [1, 2, 3, 4, 5]
    threshold3 = 3
    print(find_last_greater_equal(list3, threshold3))