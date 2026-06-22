def compute_mean(data):
    return sum(data) / len(data)

if __name__ == '__main__':
    data1 = [10, 20, 30, 40, 50]
    mean1 = compute_mean(data1)
    print(f"Data: {data1}, Mean: {mean1}")
    
    data2 = [5.5, 6.5, 7.5, 8.5, 9.5]
    mean2 = compute_mean(data2)
    print(f"Data: {data2}, Mean: {mean2}")