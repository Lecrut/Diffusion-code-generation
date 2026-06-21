def calculate_mean(values):
    if not values:
        return 0
    total = sum(values)
    count = len(values)
    return total / count

if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5]
    mean_value = calculate_mean(sample_data)
    print(mean_value)