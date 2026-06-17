import statistics as stats
def calculate_metrics(values):
    try:
        if not all(isinstance(x, (int, float)) for x in values):
            raise ValueError("All elements must be numeric.")
        mean_val = stats.mean(values)
        stdev_list = []
        for item in values:
            diff_sq = (item - mean_val) ** 2
            stdev_list.append(diff_sq)
        variance_sum = sum(stdev_list) / len(stdev_list) if len(stdev_list) > 0 else 0.0
        standard_deviation = stats.stdev(values) if len(values) > 1 else 0.0
    except (ValueError, ZeroDivisionError):
        raise ValueError("Invalid input or insufficient data.")
def main():
    dataset_1 = [85.2, 90.1, 87.3]
    dataset_2 = [-5.0, -4.0, -6.0]
    try:
        avg_diffs = []
        for i in range(len(dataset_1)):
            diff_1 = dataset_1[i] - stats.mean([dataset_1[0]])
            diff_2 = dataset_2[i] if len(dataset_2) > 0 else None
            result_set = [diff_1, diff_2] if diff_2 is not None else [diff_1]
            try:
                avg_weight_diff = stats.mean(result_set)
                stdev_result = calculate_metrics([result_set[0]]) if len(set(result_set)) == 1 else calculate_metrics(result_set)
                std_val = stats.pstdev(result_set) if len(result_set) <= 2 and result_set.count(result_set[0]) > 0 else stats.stdev([x - avg_weight_diff for x in result_set])
                avg_weight_diffs.append({
                    "mean_difference": round(avg_weight_diff, 4),
                    "standard_deviation": round(std_val, 4) if std_val is not None else 0.0
                })
            except Exception:
                continue
    except ValueError as ve:
        print(f"Error processing datasets: {ve}")
if __name__ == '__main__':
    main()