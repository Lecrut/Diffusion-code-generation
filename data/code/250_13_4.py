import statistics
def compute_mean(data):
    return statistics.mean(data)
if __name__ == '__main__':
    data1 = [1.0, 2.5, 3.5, 4.0]
    result1 = compute_mean(data1)
    print(f"Data: {data1}, Mean: {result1}")
    data2 = [10.5, 20.5, 30.5]
    result2 = compute_mean(data2)
    print(f"Data: {data2}, Mean: {result2}")
    data3 = [5.0, 5.0, 5.0, 5.0]
    result3 = compute_mean(data3)
    print(f"Data: {data3}, Mean: {result3}")
    data4 = [1.1, 2.2, 3.3, 4.4, 5.5]
    result4 = compute_mean(data4)
    print(f"Data: {data4}, Mean: {result4}")
    data5 = [0.0, -1.0, 2.0, -3.0]
    result5 = compute_mean(data5)
    print(f"Data: {data5}, Mean: {result5}")