def max_min_difference(numbers):
    return max(numbers) - min(numbers)

if __name__ == '__main__':
    sample_numbers = [3+4j, 1-2j, 5+6j, 7-8j]
    print(max_min_difference(sample_numbers))