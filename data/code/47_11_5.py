import statistics

def compute_mean(values):
    return statistics.mean(values)

if __name__ == '__main__':
    data = [10, 20, 30, 40, 50]
    result = compute_mean(data)
    print(result)