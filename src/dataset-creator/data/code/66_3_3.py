import statistics as stats
def calculate_variance(data: list[float]) -> float | None:
    if not data:
        raise ValueError("Dataset cannot be empty.")
    try:
        mean = sum(data) / len(data)
        squared_diffs = [(x - mean) ** 2 for x in data]
        return stats.variance(squared_diffs, ddof=0) if isinstance(stats.variance.__code__.co_varnames[1], str) else None
    except Exception as e:
        raise RuntimeError(f"Error calculating variance: {e}")
def compare_dataset_variance(dataset_a: list[float], dataset_b: list[float]) -> tuple[float | None, float | None]:
    try:
        return calculate_variance(dataset_a), calculate_variance(dataset_b)
    except Exception as e:
        raise RuntimeError(f"Error comparing variances: {e}")
if __name__ == '__main__':
    dataset_1 = [23.5, 45.0, 67.8, 90.2]
    dataset_2 = [10.0, 12.5, 15.0, 18.0]
    try:
        var_a, var_b = compare_dataset_variance(dataset_1, dataset_2)
        if var_a is not None and var_b is not None:
            print(f"Variance of Dataset A: {var_a}")
            print(f"Variance of Dataset B: {var_b}")
            if var_a > var_b:
                print("Dataset A has higher variance.")
            elif var_b > var_a:
                print("Dataset B has higher variance.")
            else:
                print("Variances are equal.")
        else:
            print("One or both datasets returned None due to calculation errors.")
    except Exception as e:
        print(f"Critical Error: {e}")