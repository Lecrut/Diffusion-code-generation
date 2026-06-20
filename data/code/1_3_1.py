def find_outliers(data: list[float], min_val: float, max_val: float) -> list[float]:
    return [x for x in data if x < min_val or x > max_val]

if __name__ == '__main__':
    sample_data = [49, 50, 100, 150, 199, 200, 201, 250]
    result = find_outliers(sample_data, 50, 200)
    print(result)