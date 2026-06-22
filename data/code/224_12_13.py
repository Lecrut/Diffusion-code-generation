def calculate_mean(values):
    return sum(values) / len(values)

if __name__ == '__main__':
    sample_values = [5, 10, 15, 20]
    print(calculate_mean(sample_values))