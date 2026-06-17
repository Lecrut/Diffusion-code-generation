import statistics
def compute_mean(data):
    return statistics.mean(data)
if __name__ == '__main__':
    data1 = [1.0, 2.5, 3.5, 4.0]
    print(f"Data: {data1}")
    print(f"Mean: {compute_mean(data1)}")
    data2 = [10.5, 20.5, 30.5]
    print(f"\nData: {data2}")
    print(f"Mean: {compute_mean(data2)}")
    data3 = [1.1, 2.2, 3.3, 4.4, 5.5]
    print(f"\nData: {data3}")
    print(f"Mean: {compute_mean(data3)}")
    data4 = [100.0, 50.5, 75.25]
    print(f"\nData: {data4}")
    print(f"Mean: {compute_mean(data4)}")
    data5 = [5.0]
    print(f"\nData: {data5}")
    print(f"Mean: {compute_mean(data5)}")