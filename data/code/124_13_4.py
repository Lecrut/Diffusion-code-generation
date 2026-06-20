def calculate():
    a = 5
    b = 3
    return a + b, a - b, a * b, a / b

if __name__ == '__main__':
    results = calculate()
    print("Addition:", results[0])
    print("Subtraction:", results[1])
    print("Multiplication:", results[2])
    print("Division:", results[3])