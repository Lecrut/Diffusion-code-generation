def compute_mean(values: list[float]) -> float:
    return sum(values) / len(values)

if __name__ == '__main__':
    sample_values: list[float] = [1.5, 2.3, 3.7, 4.1, 5.9]
    result: float = compute_mean(sample_values)
    print(result)