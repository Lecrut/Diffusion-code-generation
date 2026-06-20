def contains_negative(numbers):
    return any(num < 0 for num in numbers)

if __name__ == '__main__':
    sample_values = [10, -5, 0, -100]
    print(contains_negative(sample_values))