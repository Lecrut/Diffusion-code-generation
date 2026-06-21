DIVISION_BY_ZERO = 1e-09

def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    return total / (count + DIVISION_BY_ZERO) if count > 0 else 0
if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    print(calculate_average(sample_values))