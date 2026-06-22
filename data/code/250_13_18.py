def validate_data(data):
    if not data:
        raise ValueError("Data list is empty")
    if not all(isinstance(x, (int, float)) for x in data):
        raise TypeError("All elements must be numbers")

def compute_mean(data):
    validate_data(data)
    return sum(data) / len(data)

if __name__ == '__main__':
    data1 = [10.5, 20.5, 30.5]
    mean1 = compute_mean(data1)
    print(f"Data: {data1}, Mean: {mean1}")
    
    data2 = [1.0, 2.0, 3.0, 4.0, 5.0]
    mean2 = compute_mean(data2)
    print(f"Data: {data2}, Mean: {mean2}")
    
    data3 = [100.0, 50.5, 75.25]
    mean3 = compute_mean(data3)
    print(f"Data: {data3}, Mean: {mean3}")
    
    data4 = [3.14, 2.71, 1.618]
    mean4 = compute_mean(data4)
    print(f"Data: {data4}, Mean: {mean4}")