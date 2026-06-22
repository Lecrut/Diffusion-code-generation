def calculate_mean(values):
    if not values:
        raise ValueError("Cannot calculate mean of an empty list")
    return sum(values) / len(values)

if __name__ == '__main__':
    sample_values = [10.5, 20.3, 30.1, 40.8, 50.2]
    result = calculate_mean(sample_values)
    print(result)