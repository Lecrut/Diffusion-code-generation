def compute_average(data):
    return sum(data) / len(data)

if __name__ == '__main__':
    data_points = [2.3, 4.5, 6.7, 8.9]
    average_value = compute_average(data_points)
    print(average_value)