import statistics

def compute_mean(data):
    return statistics.mean(data)

if __name__ == '__main__':
    values = [10, 20, 30, 40, 50]
    result = compute_mean(values)
    print(result)