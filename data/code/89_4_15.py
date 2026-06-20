import operator

class MathOperation:
    def __init__(self):
        self.operations = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
            '**': operator.pow,
            '%': operator.mod,
            '//': operator.floordiv
        }
    
    def execute(self, num1, num2, operation):
        return self.operations[operation](num1, num2)

if __name__ == '__main__':
    evaluator = MathOperation()
    result_add = evaluator.execute(10, 5, '+')
    result_sub = evaluator.execute(10, 5, '-')
    result_mul = evaluator.execute(10, 5, '*')
    result_div = evaluator.execute(10, 5, '/')
    result_pow = evaluator.execute(2, 3, '**')
    result_mod = evaluator.execute(10, 3, '%')
    result_floordiv = evaluator.execute(10, 3, '//')

    print(result_add)
    print(result_sub)
    print(result_mul)
    print(result_div)
    print(result_pow)
    print(result_mod)
    print(result_floordiv)