def compute_mean(data):
    if not data:
        raise ValueError("Data list cannot be empty")
    
    return sum(data) / len(data)

if __name__ == '__main__':
    data1 = [10.5, 20.5, 30.5]
    print(f"Data: {data1}, Mean: {compute_mean(data1)}")
    
    data2 = [1.0, 2.0, 3.0, 4.0, 5.0]
    print(f"Data: {data2}, Mean: {compute_mean(data2)}")
    
    data3 = [100.0, 50.5, 75.25]
    print(f"Data: {data3}, Mean: {compute_mean(data3)}")
    
    data4 = [3.14, 2.71, 1.618]
    print(f"Data: {data4}, Mean: {compute_mean(data4)}")