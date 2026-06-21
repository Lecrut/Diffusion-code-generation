def _validate_boolean(value):
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean")

def check_logic(A, B, C):
    _validate_boolean(A)
    _validate_boolean(B)
    _validate_boolean(C)
    inner_or = B or (not C)
    final_result = A and inner_or
    return final_result

if __name__ == '__main__':
    val_A = True
    val_B = False
    val_C = True
    computed_result = check_logic(val_A, val_B, val_C)
    print(computed_result)