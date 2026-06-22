def validate_input(values):
    if not all(isinstance(x, int) for x in values):
        raise ValueError("All inputs must be integers")
    return True

def sum_of_integers():
    numbers = [-10, -5, 0, 5, 10, 15]
    if not validate_input(numbers):
        return None
    total = sum(numbers)
    return total

if __name__ == '__main__':
    result = sum_of_integers()
    print(f"Sum of (-10, -5, 0, 5, 10, 15): {result}")