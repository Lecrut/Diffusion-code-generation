def validate_inputs(a: int, b: int):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both inputs must be integers.")
    if abs(a) > 1000 or abs(b) > 1000:
        raise ValueError("Inputs must be within the range -1000 to 1000.")

def add_numbers(a: int, b: int) -> int:
    validate_inputs(a, b)
    return a + b

if __name__ == '__main__':
    result = add_numbers(5, 3)
    print(result)