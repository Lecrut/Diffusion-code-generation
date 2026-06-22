def max_min_diff(complex_numbers):
    return max(complex_numbers) - min(complex_numbers)

if __name__ == '__main__':
    sample_values = [3+4j, 1-2j, 5+6j, 7-8j]
    print(max_min_diff(sample_values))