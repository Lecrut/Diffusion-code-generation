def arithmetic_operations(numbers):
    result = 0
    for number in numbers:
        if isinstance(number, (int, float)):
            result += number
        else:
            raise ValueError("Invalid input: all elements must be numbers")
    return result

if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40]
    print(arithmetic_operations(sample_numbers))