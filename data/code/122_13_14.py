def calculate_mean(values):
    return sum(values) / len(values)

if __name__ == '__main__':
    example_values = [2.5, 3.6, 4.7, 5.8]
    mean_value = calculate_mean(example_values)
    print(mean_value)