def compute_mean(values: list[int]) -> float:
    if not values:
        return 0.0
    total = sum(values)
    count = len(values)
    return total / count

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    result = compute_mean(sample_data)
    print(result)