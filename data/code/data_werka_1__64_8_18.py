def find_last_greater_equal(data, threshold):
    index = -1
    for i in range(len(data) - 1, -1, -1):
        if data[i] >= threshold:
            index = i
            break
    return index

if __name__ == '__main__':
    sample_list = [7, 14, 21, 28, 35, 42]
    target_threshold = 28
    print(find_last_greater_equal(sample_list, target_threshold))
    
    another_list = [10, 20, 30, 40, 50, 60, 70]
    another_threshold = 45
    print(find_last_greater_equal(another_list, another_threshold))
    
    test_list = [5, 10, 15, 20, 25, 30]
    test_threshold = 25
    print(find_last_greater_equal(test_list, test_threshold))