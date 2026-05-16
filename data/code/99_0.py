def calculate_expression(a, b, c, d):
    result = a + b * c - d / 2
    result = result // 3 + a % b
    result = result ** 2 + c * d
    return result
if __name__ == '__main__':
    val_a = 10
    val_b = 5
    val_c = 3
    val_d = 2
    final_result = calculate_expression(val_a, val_b, val_c, val_d)
    print(f"Value A: {val_a}")
    print(f"Value B: {val_b}")
    print(f"Value C: {val_c}")
    print(f"Value D: {val_d}")
    print(f"Final Result of nested operations: {final_result}")