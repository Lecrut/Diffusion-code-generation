import statistics

def compute_mean(values):
    return statistics.mean(values)

if __name__ == '__main__':
    sample_values = [85, 92, 78, 95, 88, 76, 91, 84, 89, 93]
    mean_result = compute_mean(sample_values)
    print(mean_result)