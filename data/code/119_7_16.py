def validate_inputs(a: float, b: float) -> None:
    if not isinstance(a, float) or not isinstance(b, float):
        raise ValueError("Both arguments must be floats")

def reverse_order(a: float, b: float) -> (float, float):
    validate_inputs(a, b)
    return b, a

if __name__ == '__main__':
    print(reverse_order(3.14, 2.71))