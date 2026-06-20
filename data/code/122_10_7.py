import statistics

def compute_mean(data):
    return statistics.mean(data)

if __name__ == '__main__':
    data_points = [2.5, 3.7, 4.1, 5.9]
    result = compute_mean(data_points)
    print(result)