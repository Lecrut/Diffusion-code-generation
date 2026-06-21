def compute_average(data):
    total = sum(data)
    count = len(data)
    average = total / count if count > 0 else 0
    return average

if __name__ == '__main__':
    data_points = [3.5, 2.1, 4.8, 5.9]
    avg = compute_average(data_points)
    print(avg)