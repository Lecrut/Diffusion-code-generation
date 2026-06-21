def calculate_mean(values):
    return sum(values) / len(values)

if __name__ == '__main__':
    sample_values = (3, 5, 7, 9)
    print(calculate_mean(sample_values))