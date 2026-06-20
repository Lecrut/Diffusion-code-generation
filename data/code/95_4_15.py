def check_numbers(numbers):
    count = 0
    for num in numbers:
        if num > 0 and num % 2 == 0 and num % 4 == 0:
            count += 1
    return count >= 3

if __name__ == '__main__':
    sample_values = [4, -2, 8, 6, 10]
    print(check_numbers(sample_values))