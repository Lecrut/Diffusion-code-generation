import statistics as stats
def compute_stats(data_list):
    try:
        if not data_list:
            return None
        averages = []
        for dataset in data_list:
            avg = sum(dataset) / len(dataset)
            stdev = stats.stdev(dataset) if len(dataset) > 1 else 0.0
            try:
                float(sum(dataset))
            except TypeError:
                return None
            averages.append({
                'average': avg,
                'standard_deviation': stdev
            })
        return averages
    except Exception as e:
        print(f"Error computing statistics: {e}")
        return None
if __name__ == '__main__':
    datasets = [
        [10.5, 20.3, 19.8],
        [5.2, 6.7, 4.9, 5.1],
        ['invalid', 'data']
    ]
    results = compute_stats(datasets)
    if results:
        for i, result in enumerate(results):
            print(f"Dataset {i + 1}: Average={result['average']:.2f}, StdDev={result['standard_deviation']:.2f}")
    else:
        print("Invalid data detected.")