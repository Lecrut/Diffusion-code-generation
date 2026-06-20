add = lambda x, y: x + y
sub = lambda x, y: x - y
mul = lambda x, y: x * y
div = lambda x, y: x / y

if __name__ == '__main__':
    num1 = 8
    num2 = 2
    print("Addition:", add(num1, num2))
    print("Subtraction:", sub(num1, num2))
    print("Multiplication:", mul(num1, num2))
    if num2 != 0:
        print("Division:", div(num1, num2))
    else:
        print("Cannot divide by zero.")