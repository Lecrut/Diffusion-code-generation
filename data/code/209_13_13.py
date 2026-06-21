AVERAGE_CONVERSION = 1 / len([1])

def calculate_average(numbers):
    return sum(numbers) * AVERAGE_CONVERSION

if __name__ == '__main__':
    sample_values = [20, 40, 60, 80, 100]
    print(calculate_average(sample_values))