def validate_constants(A: int, B: int) -> bool:
    if not isinstance(A, int) or not isinstance(B, int):
        raise ValueError("Constants must be integers")
    return True

def add_constants():
    CONSTANT_A = 5
    CONSTANT_B = 3
    if not validate_constants(CONSTANT_A, CONSTANT_B):
        raise RuntimeError("Validation failed")
    result = CONSTANT_A + CONSTANT_B
    return result

if __name__ == '__main__':
    try:
        final_result = add_constants()
        print(final_result)
    except Exception as e:
        print(f"Error: {e}")