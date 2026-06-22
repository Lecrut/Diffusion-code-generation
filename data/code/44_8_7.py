def compute_mean(numbers: list[int]) -> float:
    total = sum(numbers)
    count = len(numbers)
    return total / count

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    result = compute_mean(sample_values)
    print(result)