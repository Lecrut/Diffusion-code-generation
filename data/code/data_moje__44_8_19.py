import statistics

def compute_mean(data: list[int]) -> float:
    if not data:
        raise ValueError("List must not be empty")
    return statistics.mean(data)

if __name__ == '__main__':
    sample_values: list[int] = [10, 20, 30, 40, 50]
    result: float = compute_mean(sample_values)
    print(result)