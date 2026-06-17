import statistics
def calculate_mean(data):
    return statistics.mean(data)
if __name__ == '__main__':
    data1 = [10.5, 20.5, 30.5]
    print(f"Data: {data1}, Mean: {calculate_mean(data1)}")
    data2 = [1.0, 2.0, 3.0, 4.0, 5.0]
    print(f"Data: {data2}, Mean: {calculate_mean(data2)}")
    data3 = [100.0, 50.5, 75.25]
    print(f"Data: {data3}, Mean: {calculate_mean(data3)}")
    data4 = [3.14159, 2.71828, 1.61803]
    print(f"Data: {data4}, Mean: {calculate_mean(data4)}")
    data5 = [5.0]
    print(f"Data: {data5}, Mean: {calculate_mean(data5)}")