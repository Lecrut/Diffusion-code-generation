def and_op(a, b):
    return a and b
def or_op(a, b):
    return a or b
def not_op(a):
    return not a
def complex_expression(a, b, c):
    result_and = and_op(a, b)
    result_or = or_op(result_and, c)
    result_not = not_op(result_or)
    return result_not
if __name__ == '__main__':
    val_a = True
    val_b = False
    val_c = True
    final_result = complex_expression(val_a, val_b, val_c)
    print(f"Value A: {val_a}")
    print(f"Value B: {val_b}")
    print(f"Value C: {val_c}")
    print(f"Complex Expression Result: {final_result}")