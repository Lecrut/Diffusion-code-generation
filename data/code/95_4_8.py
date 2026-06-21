def check_conditions(numbers):
    count = 0
    for num in numbers:
        if num > 0 and num % 2 == 0:
            count += 1
    return count >= 3

if __name__ == '__main__':
    sample_numbers = [2, 4, 6, 8, 10]
    result = check_conditions(sample_numbers)
    print(result)