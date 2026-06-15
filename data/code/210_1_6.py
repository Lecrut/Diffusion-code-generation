def find_data_range(data):
    if not data:
        return 0.0
    minimum = data[0]
    maximum = data[0]
    for x in data:
        if x < minimum:
            minimum = x
        if x > maximum:
            maximum = x
    return maximum - minimum
if __name__ == '__main__':
    sample_data1 = [1.5, 3.2, 0.9, 5.8, 2.1]
    result1 = find_data_range(sample_data1)
    print(f"Data: {sample_data1}, Range: {result1}")
    sample_data2 = [10.0, 5.0, 20.0, 15.0]
    result2 = find_data_range(sample_data2)
    print(f"Data: {sample_data2}, Range: {result2}")
    sample_data3 = [7.7]
    result3 = find_data_range(sample_data3)
    print(f"Data: {sample_data3}, Range: {result3}")
    sample_data4 = []
    result4 = find_data_range(sample_data4)
    print(f"Data: {sample_data4}, Range: {result4}")