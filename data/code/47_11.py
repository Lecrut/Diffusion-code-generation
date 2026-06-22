import statistics

def compute_mean(results):
    return statistics.mean(results)

if __name__ == '__main__':
    sample_results = [85, 92, 78, 95, 88, 76, 91, 84, 90, 87]
    mean_value = compute_mean(sample_results)
    print(mean_value)