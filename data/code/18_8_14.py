def get_middle_value(numbers):
    if not numbers:
        return None
    return numbers[len(numbers) // 2]

if __name__ == '__main__':
    test_data = [10, 20, 30, 40, 50]
    result = get_middle_value(test_data)
    print(result)