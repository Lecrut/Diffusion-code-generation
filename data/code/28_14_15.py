def _validate_numeric(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be numbers")

def sort_two_numbers(a, b):
    _validate_numeric(a, b)
    return (a, b) if a <= b else (b, a)

if __name__ == '__main__':
    FIRST_VAL = 42.5
    SECOND_VAL = 10.2
    result = sort_two_numbers(FIRST_VAL, SECOND_VAL)
    print(result)
    ANOTHER_A = -5
    ANOTHER_B = -20
    print(sort_two_numbers(ANOTHER_A, ANOTHER_B))
    print(sort_two_numbers(100, 100))