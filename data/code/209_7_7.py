def compute_mean(data: list[float]) -> float:
    if not data:
        return 0.0
    return sum(data) / len(data)

if __name__ == '__main__':
    sample_data = [7.7, 8.8, 9.9]
    mean_value = compute_mean(sample_data)
    print(mean_value)