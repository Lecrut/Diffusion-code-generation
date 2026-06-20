import ast
import operator

def evaluate_boolean_expression(expression):
    ops = {ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul, ast.Div: operator.truediv, ast.USub: operator.neg, ast.And: lambda x, y: x and y, ast.Or: lambda x, y: x or y, ast.Not: operator.not_, ast.Eq: operator.eq, ast.Gt: operator.gt, ast.Lt: operator.lt}

    def eval_node(node):
        if isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, ast.BinOp):
            return ops[type(node.op)](eval_node(node.left), eval_node(node.right))
        elif isinstance(node, ast.UnaryOp):
            return ops[type(node.op)](eval_node(node.operand))
        else:
            raise TypeError(repr(node))
    try:
        node = ast.parse(expression, mode='eval').body
        return eval_node(node)
    except Exception as e:
        print(f'Error evaluating expression: {e}')
        return None
if __name__ == '__main__':
    result = evaluate_boolean_expression('3 > 2 and 5 < 10')
    print(result)