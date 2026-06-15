import statistics
def calculate_mean(data):
    return statistics.mean(data)
if __name__ == '__main__':
    data1 = [1.0, 2.5, 3.5, 4.0]
    mean1 = calculate_mean(data1)
    print(f"Data: {data1}, Mean: {mean1}")
    data2 = [10.5, 20.5, 30.5]
    mean2 = calculate_mean(data2)
    print(f"Data: {data2}, Mean: {mean2}")
    data3 = [5.0, 5.0, 5.0, 5.0]
    mean3 = calculate_mean(data3)
    print(f"Data: {data3}, Mean: {mean3}")
    data4 = [1.1, 2.2, 3.3, 4.4, 5.5]
    mean4 = calculate_mean(data4)
    print(f"Data: {data4}, Mean: {mean4}")