def evaluate_boolean_expression(expression):
    def _eval(node, variables):
        if isinstance(node, ast.Expression):
            return _eval(node.body, variables)
        elif isinstance(node, ast.Constant):
            return node.value
        elif isinstance(node, ast.Name):
            return variables[node.id]
        elif isinstance(node, ast.BinOp):
            left = _eval(node.left, variables)
            right = _eval(node.right, variables)
            if isinstance(node.op, ast.And):
                return left and right
            elif isinstance(node.op, ast.Or):
                return left or right
        elif isinstance(node, ast.UnaryOp):
            operand = _eval(node.operand, variables)
            if isinstance(node.op, ast.Not):
                return not operand

    tree = ast.parse(expression, mode='eval').body
    variables = {}
    return _eval(tree, variables)

if __name__ == '__main__':
    print(evaluate_boolean_expression('(True and False) or (not True)'))
    print(evaluate_boolean_expression('not (False or True) and True'))
    print(evaluate_boolean_expression('True and not (False and True)'))
    print(evaluate_boolean_expression('(True or False) and (not False)'))