def check_conditions(numbers):
    return all(num > 0 for num in numbers) and any(num % 2 == 0 for num in numbers)

if __name__ == '__main__':
    sample_numbers = [2, 4, 6, 8]
    print(check_conditions(sample_numbers))