import statistics

def compute_average(data):
    return statistics.mean(data)

if __name__ == '__main__':
    dataset = [10, 20, 30, 40, 50]
    avg_result = compute_average(dataset)
    print(avg_result)