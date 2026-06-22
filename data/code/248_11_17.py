def add_floats(a: float, b: float) -> float:
    return round(a + b, 15)

if __name__ == '__main__':
    num1 = 3.141592653589793
    num2 = 2.718281828459045
    result = add_floats(num1, num2)
    print(result)