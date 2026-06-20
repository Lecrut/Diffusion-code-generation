def validate_inputs(a: int, b: int) -> None:
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both inputs must be integers.")
    if a <= 0 or b <= 0:
        raise ValueError("Inputs must be positive integers.")

def calculate_gcd(a: int, b: int) -> int:
    validate_inputs(a, b)
    while b != 0:
        a, b = b, a % b
    return a

if __name__ == '__main__':
    result = calculate_gcd(48, 18)
    print(result)