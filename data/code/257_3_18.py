def complex_diff(numbers):
    return max(numbers) - min(numbers)

if __name__ == '__main__':
    sample_values = [3+4j, 1-2j, 5+6j, -7+8j]
    print(complex_diff(sample_values))