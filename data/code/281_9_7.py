def validate_input(numbers):
    if not isinstance(numbers, set) or len(numbers) != 12:
        raise ValueError("Input must be a set of exactly twelve numbers")

def sum_of_twelve_numbers():
    numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
    validate_input(numbers)
    return sum(numbers)

if __name__ == '__main__':
    result = sum_of_twelve_numbers()
    print(result)