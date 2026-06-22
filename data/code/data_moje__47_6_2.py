def compute_mean(values: list[float]) -> float:
    return sum(values) / len(values)

if __name__ == '__main__':
    sample_values = [1.5, 2.7, 3.2, 4.8, 5.1]
    result = compute_mean(sample_values)
    print(result)