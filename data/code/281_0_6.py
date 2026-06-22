def validate_numbers(numbers):
    if not isinstance(numbers, list) or len(numbers) != 3:
        raise ValueError("Input must be a list of exactly three integers")
    for num in numbers:
        if not isinstance(num, int):
            raise ValueError("All elements in the list must be integers")

def sum_three(a, b, c):
    validate_numbers([a, b, c])
    return a + b + c

if __name__ == '__main__':
    result = sum_three(10, 25, 30)
    print(result)