def compute_mean(values: list[int]) -> float:
    total = 0
    for value in values:
        total += value
    return total / len(values)

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    result = compute_mean(sample_values)
    print(result)