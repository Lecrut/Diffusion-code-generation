import statistics as stats
def compute_stats(values):
    try:
        if not isinstance(values, list) or len(values) == 0:
            return None, "Input must be a non-empty list of numbers."
        for item in values:
            if not isinstance(item, (int, float)):
                return None, f"Invalid input type. Expected number, got {type(item).__name__}."
    except Exception as e:
        return None, str(e)
    mean = stats.mean(values)
    stdev = stats.stdev(values) if len(values) > 1 else float('inf')
    return mean, stdev
def main():
    datasets = [
        [70.5, 68.2, 72.1],
        ["invalid", 74.3, 71.9],
        [65.0, 66.0]
    ]
    for i, data in enumerate(datasets):
        mean_val, stdev_val = compute_stats(data)
        if not isinstance(mean_val, float):
            print(f"Dataset {i}: Error - {mean_val}")
        else:
            print(f"Dataset {i} Mean Weight Difference: {mean_val:.2f}, Standard Deviation: {stdev_val:.2f}")
if __name__ == '__main__':
    main()