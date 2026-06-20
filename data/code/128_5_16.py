def has_negative(numbers):
    return any(num < 0 for num in numbers)

if __name__ == '__main__':
    sample_values = [1, -2, 3, 4, 5]
    print(has_negative(sample_values))