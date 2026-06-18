import statistics as stats
def compute_stats(data_list):
    try:
        if not data_list:
            return None, "Error: Empty dataset"
        averages = []
        for i in range(len(data_list)):
            avg_val = sum(data_list[i]) / len(data_list[i])
            try:
                std_dev = stats.stdev(data_list[i])
            except ValueError:
                std_dev = None
            averages.append({
                'average': avg_val,
                'standard_deviation': std_dev
            })
        return averages, "Success"
    except Exception as e:
        return None, f"Error processing data: {str(e)}"
if __name__ == '__main__':
    datasets = [
        [10.5, 20.3, 30.7],
        [45.2, 56.8, 67.9],
        [100]
    ]
    results, message = compute_stats(datasets)
    if isinstance(results, list):
        print(f"Status: {message}")
        for i, stat in enumerate(results):
            avg_info = f"Dataset {i+1}: Average Weight Difference = {stat['average']}"
            std_info = ""
            if stat['standard_deviation']:
                std_info += f", Standard Deviation = {stat['standard_deviation']}"
            print(avg_info + std_info)
    else:
        print(f"Status: {message}")