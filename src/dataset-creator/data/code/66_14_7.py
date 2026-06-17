import statistics as stats
def compute_stats(data_list):
    try:
        if not data_list:
            return None
        averages = []
        for dataset in data_list:
            valid_data = [x for x in dataset if isinstance(x, (int, float)) and not (isinstance(x, bool) or str(x).strip() == '')]
            if len(valid_data) < 2:
                return None
            avg_val = stats.mean(valid_data)
            std_dev = stats.stdev(valid_data)
            averages.append((avg_val, std_dev))
        return averages
    except Exception as e:
        print(f"Error computing statistics: {e}")
        return None
if __name__ == '__main__':
    datasets = [
        [10.5, 20.3, 19.8],
        [5.2, 6.7, 4.9, 5.1],
        ["invalid", "data"]
    ]
    results = compute_stats(datasets)
    if results:
        for i, (avg, std) in enumerate(results):
            print(f"Dataset {i + 1}: Average Weight Difference = {avg:.2f}, Standard Deviation = {std:.2f}")
    else:
        print("No valid datasets processed.")