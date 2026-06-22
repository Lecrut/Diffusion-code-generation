def validate_input(numbers):
    if not all(isinstance(num, int) for num in numbers):
        raise ValueError("All inputs must be integers")
    if len(numbers) != 6:
        raise ValueError("Exactly six numbers are required")

def sum_of_integers():
    numbers = [-10, -5, 0, 5, 10, 15]
    validate_input(numbers)
    return sum(numbers)

if __name__ == '__main__':
    result = sum_of_integers()
    print(f"Sum of (-10, -5, 0, 5, 10, 15): {result}")