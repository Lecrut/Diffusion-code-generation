import sys
def compare_floats(a, b):
    try:
        float_a = float(a)
        float_b = float(b)
        if float_a > float_b:
            return f"Float {a} is larger than Float {b}"
        elif float_b > float_a:
            return f"Float {b} is larger than Float {a}"
        else:
            return f"Float {a} and Float {b} are equal"
    except ValueError:
        return "Error: Both inputs must be valid floating-point numbers."
if __name__ == '__main__':
    num1 = "3.14159"
    num2 = "2.71828"
    result = compare_floats(num1, num2)
    print(result)
    num3 = "10.5"
    num4 = "-5.2"
    result2 = compare_floats(num3, num4)
    print(result2)
    num5 = "abc"
    num6 = "4.0"
    result3 = compare_floats(num5, num6)
    print(result3)