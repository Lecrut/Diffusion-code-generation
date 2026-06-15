import statistics
def calculate_mean(data):
    return statistics.mean(data)
if __name__ == '__main__':
    data1 = [1.0, 2.5, 3.5, 4.0]
    print(f"Data: {data1}, Mean: {calculate_mean(data1)}")
    data2 = [10.5, 20.5, 30.5]
    print(f"Data: {data2}, Mean: {calculate_mean(data2)}")
    data3 = [1.1, 2.2, 3.3, 4.4, 5.5]
    print(f"Data: {data3}, Mean: {calculate_mean(data3)}")
    data4 = [5.0, 5.0, 5.0, 5.0]
    print(f"Data: {data4}, Mean: {calculate_mean(data4)}")
    data5 = [100.0, 200.0, 300.0]
    print(f"Data: {data5}, Mean: {calculate_mean(data5)}")