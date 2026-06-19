def find_last_greater_equal(data, threshold):
    if not isinstance(data, list):
        raise ValueError("Data must be a list.")
    if not all(isinstance(x, (int, float)) for x in data):
        raise ValueError("All elements in data must be numbers.")
    if not isinstance(threshold, (int, float)):
        raise ValueError("Threshold must be a number.")
    
    result = -1
    for i in range(len(data) - 1, -1, -1):
        if data[i] >= threshold:
            result = i
            break
    return result

if __name__ == '__main__':
    sample_data1 = [50, 40, 30, 20, 10]
    sample_threshold1 = 25
    print(find_last_greater_equal(sample_data1, sample_threshold1))

    sample_data2 = [1, 3, 5, 7, 9]
    sample_threshold2 = 6
    print(find_last_greater_equal(sample_data2, sample_threshold2))

    sample_data3 = [100, 200, 300, 400, 500]
    sample_threshold3 = 500
    print(find_last_greater_equal(sample_data3, sample_threshold3))