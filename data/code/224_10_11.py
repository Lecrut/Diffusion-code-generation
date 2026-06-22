def calculate_mean(values):
    total = sum(values)
    count = len(values)
    if count == 0:
        return 0
    return total / count

if __name__ == '__main__':
    sample_values = [1.5, 2.5, 3.5]
    mean_value = calculate_mean(sample_values)
    print(f"Mean of {sample_values}: {mean_value}")