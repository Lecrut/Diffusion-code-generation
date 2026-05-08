def calculate_expression(a, b, c, d):
    result = a + b * c - d / 2
    result = result // 3 + a % b
    result = result ** 2
    return result
if __name__ == '__main__':
    a = 10
    b = 5
    c = 3
    d = 2
    print("--- Demonstrating Order of Operations ---")
    print(f"Input values: a={a}, b={b}, c={c}, d={d}")
    result = calculate_expression(a, b, c, d)
    print("\nStep-by-step calculation based on the function logic:")
    intermediate1 = a + b * c - d / 2
    print(f"Step 1 (a + b * c - d / 2): {intermediate1}")
    intermediate2 = intermediate1 // 3 + a % b
    print(f"Step 2 (intermediate1 // 3 + a % b): {intermediate2}")
    final_result = intermediate2 ** 2
    print(f"Step 3 (intermediate2 ** 2): {final_result}")
    print("\nFinal Result:")
    print(final_result)