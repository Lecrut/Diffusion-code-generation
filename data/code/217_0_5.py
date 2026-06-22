def validate_input(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both arguments must be integers.")

def compare_integers(a, b):
    validate_input(a, b)
    if a > b:
        return "greater than"
    elif a < b:
        return "less than"
    else:
        return "equal to"

if __name__ == '__main__':
    result = compare_integers(10, 5)
    print(result)