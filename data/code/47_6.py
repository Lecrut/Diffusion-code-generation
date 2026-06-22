def compute_mean(values: list[float]) -> float:
    if not values:
        return 0.0
    return sum(values) / len(values)

if __name__ == '__main__':
    sample_values = [10.5, 20.3, 30.1, 40.7, 50.9]
    result = compute_mean(sample_values)
    print(result)