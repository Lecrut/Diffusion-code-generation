def has_three_positive_even_divisible_by_two(numbers):
    if not isinstance(numbers, (list, tuple)):
        raise ValueError("Input must be a list or tuple")
    
    count = 0
    for n in numbers:
        if n > 0 and n % 2 == 0:
            count += 1
            if count >= 3:
                return True
    return False

if __name__ == '__main__':
    test_data = [2, 4, 6, -1, 0, 8, 10]
    result = has_three_positive_even_divisible_by_two(test_data)
    print(result)