def contains_negative(numbers):
    for num in numbers:
        if num < 0:
            return True
    return False

if __name__ == '__main__':
    test_cases = [10, -5, 0, -100]
    result = contains_negative(test_cases)
    print(result)