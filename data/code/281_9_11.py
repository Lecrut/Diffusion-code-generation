def validate_numbers(numbers):
    if len(numbers) != 12:
        raise ValueError("Set must contain exactly twelve numbers.")
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise TypeError("All elements in the set must be numbers.")

def sum_of_twelve_numbers():
    numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
    validate_numbers(numbers)
    return sum(numbers)

if __name__ == '__main__':
    result = sum_of_twelve_numbers()
    print(result)