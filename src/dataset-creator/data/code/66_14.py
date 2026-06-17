import statistics as stats
def compute_stats(data_list):
    try:
        averages = []
        for dataset in data_list:
            if not isinstance(dataset, (list, tuple)):
                raise ValueError(f"Invalid input type: {type(dataset)}")
            if len(dataset) == 0:
                raise ValueError("Dataset cannot be empty.")
            avg_weight_diffs = stats.mean([abs(x - sum(dataset)/len(dataset)) for x in dataset])
            stdev_weights = stats.stdev(dataset) if len(dataset) > 1 else 0
            averages.append({
                'average_difference': round(avg_weight_diffs, 2),
                'standard_deviation': round(stdev_weights, 2)
            })
        return averages
    except Exception as e:
        raise RuntimeError(f"Error computing statistics: {str(e)}")
if __name__ == '__main__':
    datasets = [
        [10.5, 11.2, 9.8],
        [23.4, 24.1, 22.9, 25.0]
    ]
    try:
        results = compute_stats(datasets)
        print("Computed Statistics:")
        for result in results:
            print(f"Average Difference: {result['average_difference']}, Standard Deviation: {result['standard_deviation']}")
    except RuntimeError as err:
        print(err)