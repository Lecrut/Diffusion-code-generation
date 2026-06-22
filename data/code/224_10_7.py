def compute_mean(values):
    return sum(values) / len(values)

if __name__ == '__main__':
    sample_values = [1.5, 2.5, 3.5]
    print(compute_mean(sample_values))