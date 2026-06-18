import statistics as stats
def compute_stats(data_list):
    try:
        if not data_list:
            return None
        averages = []
        for dataset in data_list:
            if isinstance(dataset, list) and len(dataset) > 0:
                avg = stats.mean(dataset)
                stdev = stats.stdev(dataset) if len(dataset) > 1 else float('inf')
                averages.append((avg, stdev))
        return averages
    except Exception as e:
        print(f"Error processing data: {e}")
        return None
if __name__ == '__main__':
    datasets = [
        [70.5, 68.2, 71.3],
        [45.0, 46.5, 44.8],
        [90.1]
    ]
    result = compute_stats(datasets)
    if result:
        for i, (avg, stdev) in enumerate(result):
            print(f"Dataset {i + 1}: Average Weight Difference = {avg:.2f}, Standard Deviation = {stdev}")
    else:
        print("No valid datasets processed.")