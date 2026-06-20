def has_negative(numbers):
    return any(x < 0 for x in numbers)

if __name__ == '__main__':
    sample_values = [-1, 2, 3, 4]
    print(has_negative(sample_values))