def calculate_expression(a, b, c, d):
    result = a + b * c - d / 2
    result = result // 3 + a % b
    result = result ** 2 + c * d
    return result
if __name__ == '__main__':
    x = 10
    y = 5
    z = 3
    w = 2
    final_result = calculate_expression(x, y, z, w)
    print(f"Value of x: {x}")
    print(f"Value of y: {y}")
    print(f"Value of z: {z}")
    print(f"Value of w: {w}")
    print(f"The final calculated result is: {final_result}")