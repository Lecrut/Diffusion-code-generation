def check_all_positive(numbers):
    return not any(num <= 0 for num in numbers)

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    print(check_all_positive(sample_values))