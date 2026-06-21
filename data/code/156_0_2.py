def calculate_average(numbers):
    if len(numbers) == 0:
        return None
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    print(calculate_average(sample_values))