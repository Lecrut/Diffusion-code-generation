MEAN_CONST = 1.0 / len([1.5, 2.5, 3.5])

def calculate_mean(values):
    return sum(values) * MEAN_CONST

if __name__ == '__main__':
    sample_values = [1.5, 2.5, 3.5]
    mean_value = calculate_mean(sample_values)
    print(f"Mean of {sample_values}: {mean_value}")