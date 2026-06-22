def compute_mean(values: list[float]) -> float:
    return sum(values) / len(values)

if __name__ == '__main__':
    sample_values: list[float] = [1.5, 2.7, 3.9, 4.1, 5.8]
    result: float = compute_mean(sample_values)
    print(result)