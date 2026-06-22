def _validate_operand(value, name):
    if value is None:
        return False
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        return value != 0
    if isinstance(value, str):
        return len(value) > 0
    if isinstance(value, (list, tuple, dict, set)):
        return len(value) > 0
    return bool(value)

def evaluate_or(left, right):
    left_valid = _validate_operand(left, "left")
    right_valid = _validate_operand(right, "right")
    if left_valid:
        return left
    if right_valid:
        return right
    if not left_valid and not right_valid:
        return left if left is None or left == 0 or left == "" or left == False or left == [] else right
    return right

def resolve_or_condition(a, b):
    if _validate_operand(a, "a"):
        return a
    if _validate_operand(b, "b"):
        return b
    return a

if __name__ == '__main__':
    val_a = 0
    val_b = 0
    result_a = resolve_or_condition(val_a, val_b)
    print(result_a)
    val_c = 0
    val_d = 5
    result_b = resolve_or_condition(val_c, val_d)
    print(result_b)
    val_e = ""
    val_f = "truth"
    result_c = resolve_or_condition(val_e, val_f)
    print(result_c)
    val_g = None
    val_h = 42
    result_d = resolve_or_condition(val_g, val_h)
    print(result_d)