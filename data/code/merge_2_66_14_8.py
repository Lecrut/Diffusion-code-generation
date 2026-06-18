import statistics as stats
def calculate_stats(data_list):
    try:
        if not data_list:
            raise ValueError("Data list cannot be empty.")
        averages = []
        for dataset in data_list:
            if not isinstance(dataset, (list, tuple)):
                raise TypeError(f"Invalid input type: {type(dataset)}. Expected a sequence of numbers.")
            valid_numbers = [x for x in dataset if isinstance(x, (int, float)) and not (isinstance(x, bool))]
            if len(valid_numbers) == 0:
                continue
            avg_val = stats.mean(valid_numbers)
            std_dev = stats.stdev(valid_numbers) if len(valid_numbers) > 1 else None
            averages.append({
                'dataset': dataset,
                'average_weight_difference': round(avg_val, 2),
                'standard_deviation': round(std_dev, 2) if std_dev is not None else "N/A"
            })
        return averages
    except Exception as e:
        raise ValueError(f"An error occurred during calculation: {str(e)}")
if __name__ == '__main__':
    sample_datasets = [
        [10, 20, 30],
        [5.5, 6.7, 4.9],
        ["invalid", "data"],
        []
    ]
    try:
        results = calculate_stats(sample_datasets)
        for result in results:
            print(f"Dataset: {result['dataset']}")
            print(f"Avg Difference: {result['average_weight_difference']}")
            print(f"Std Deviation: {result['standard_deviation']}")
    except ValueError as ve:
        print(f"{ve}")