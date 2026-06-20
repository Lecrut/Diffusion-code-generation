class MathOperations:
    def __init__(self):
        self.add = lambda x, y: x + y
        self.sub = lambda x, y: x - y
        self.mul = lambda x, y: x * y
        self.div = lambda x, y: x / y

if __name__ == '__main__':
    math_ops = MathOperations()
    print(math_ops.add(8, 2))
    print(math_ops.sub(8, 2))
    print(math_ops.mul(8, 2))
    print(math_ops.div(8, 2))