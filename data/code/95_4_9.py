def check_numbers(numbers):
    count = 0
    for num in numbers:
        if num > 0 and num % 2 == 0 and num % 2 == 0:
            count += 1
        if count >= 3:
            return True
    return False

if __name__ == '__main__':
    sample_values = [1, 2, 4, 6, 8]
    print(check_numbers(sample_values))