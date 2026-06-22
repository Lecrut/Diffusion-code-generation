def complex_diff(numbers):
    return max(numbers) - min(numbers)

if __name__ == '__main__':
    sample_numbers = [3+4j, 1-2j, 5+6j, 0+0j]
    print(complex_diff(sample_numbers))