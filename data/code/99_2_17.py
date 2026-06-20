import operator

def evaluate_expressions(expressions):
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '**': operator.pow,
        '%': operator.mod,
        '//': operator.floordiv
    }
    
    def eval_expr(expr):
        tokens = expr.split()
        stack = []
        
        for token in tokens:
            if token.isdigit():
                stack.append(int(token))
            elif token in ops:
                b = stack.pop()
                a = stack.pop()
                result = ops[token](a, b)
                stack.append(result)
            else:
                raise ValueError(f"Unknown operator: {token}")
        
        return stack[0]
    
    return [eval_expr(expr) for expr in expressions]

if __name__ == '__main__':
    expressions = [
        "3 + 5 * 2",
        "8 / 4 - 1",
        "7 ** 2 % 3",
        "6 // 2 + 1"
    ]
    
    results = evaluate_expressions(expressions)
    print(results)