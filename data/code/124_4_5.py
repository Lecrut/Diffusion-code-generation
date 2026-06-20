add = lambda x, y: x + y
sub = lambda x, y: x - y
mul = lambda x, y: x * y
div = lambda x, y: x / y if y != 0 else 'Error: Division by zero'

if __name__ == '__main__':
    print(add(8, 2))
    print(sub(8, 2))
    print(mul(8, 2))
    print(div(8, 2))