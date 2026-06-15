import statistics
def calculate_mean(data):
    return statistics.mean(data)
if __name__ == '__main__':
    data1 = [1.5, 2.5, 3.5]
    print(f"Data: {data1}, Mean: {calculate_mean(data1)}")
    data2 = [10.0, 20.0, 30.0, 40.0]
    print(f"Data: {data2}, Mean: {calculate_mean(data2)}")
    data3 = [5.5, 6.5, 7.5, 8.5]
    print(f"Data: {data3}, Mean: {calculate_mean(data3)}")
    data4 = [1.0, 2.0, 3.0, 4.0, 5.0]
    print(f"Data: {data4}, Mean: {calculate_mean(data4)}")
    data5 = [100.5, 99.5, 101.0]
    print(f"Data: {data5}, Mean: {calculate_mean(data5)}")