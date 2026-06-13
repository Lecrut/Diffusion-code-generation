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
        return "Error: Invalid input. Both inputs must be valid floating-point numbers."
if __name__ == '__main__':
    num1 = "3.14159"
    num2 = "2.71828"
    result = compare_floats(num1, num2)
    print(result)