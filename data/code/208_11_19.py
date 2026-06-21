def calculate_mean(values):
    if not values:
        return None
    return sum(values) / len(values)

if __name__ == '__main__':
    sample_values = [10, 20.5, 30, 40.75]
    mean_value = calculate_mean(sample_values)
    print(mean_value)