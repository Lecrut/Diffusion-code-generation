def check_conditions(numbers):
    return sum(1 for num in numbers if num > 0 and num % 2 == 0 and num % 4 == 0) >= 3

if __name__ == '__main__':
    sample_numbers = [4, -2, 6, 8, 10]
    print(check_conditions(sample_numbers))