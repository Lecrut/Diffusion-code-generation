def calculate(a, b):
    try:
        add = a + b
        subtract = a - b
        multiply = a * b
        if b != 0:
            divide = a / b
        else:
            raise ValueError("Cannot divide by zero")
        return add, subtract, multiply, divide
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    result = calculate(10.5, 3.2)
    print(result)