def calculate_expression(a, b, c, d):
    result = ((a + b) * c) / (d // 2) % (a - b) ** 2
    return result
if __name__ == '__main__':
    val_a = 10
    val_b = 5
    val_c = 3
    val_d = 12
    result = calculate_expression(val_a, val_b, val_c, val_d)
    print(f"Value A: {val_a}")
    print(f"Value B: {val_b}")
    print(f"Value C: {val_c}")
    print(f"Value D: {val_d}")
    print(f"Result of nested calculation: {result}")