def calculate_mean(data):
    return sum(data) / len(data)

if __name__ == '__main__':
    data1 = [2.0, 4.0, 6.0]
    mean1 = calculate_mean(data1)
    print(f"Data: {data1}, Mean: {mean1}")
    
    data2 = [15.0, 30.0, 45.0, 60.0]
    mean2 = calculate_mean(data2)
    print(f"Data: {data2}, Mean: {mean2}")
    
    data3 = [-1.0, -2.0, -3.0, -4.0]
    mean3 = calculate_mean(data3)
    print(f"Data: {data3}, Mean: {mean3}")