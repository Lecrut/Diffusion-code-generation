def check_positive_even_divisible_by_two(numbers):
    required_count = 3
    count = sum(1 for num in numbers if num > 0 and num % 2 == 0)
    return count >= required_count

if __name__ == '__main__':
    test_data = [1, 2, 4, 6, 8, 10, 12]
    result = check_positive_even_divisible_by_two(test_data)
    print(result)