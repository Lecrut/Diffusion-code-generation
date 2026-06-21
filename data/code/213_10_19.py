import statistics

def compute_statistics(data):
    return {
        'mean': statistics.mean(data),
        'median': statistics.median(data),
        'std_dev': statistics.stdev(data)
    }

if __name__ == '__main__':
    sample_list = [10, 25, 32, 8, 45]
    stats = compute_statistics(sample_list)
    print(f"List: {sample_list}")
    for key, value in stats.items():
        print(f"{key.capitalize()}: {value:.2f}")