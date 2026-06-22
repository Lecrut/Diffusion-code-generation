import ast
import operator

def evaluate_expressions(expressions):
    results = []
    for expr in expressions:
        try:
            tree = ast.parse(expr, mode='eval')
            result = eval(compile(tree, '<string>', 'eval'))

            def get_precedence(op_node):
                if isinstance(op_node, ast.Add):
                    return 1
                elif isinstance(op_node, ast.Sub):
                    return 1
                elif isinstance(op_node, ast.Mult):
                    return 2
                elif isinstance(op_node, ast.Div):
                    return 2
                elif isinstance(op_node, ast.FloorDiv):
                    return 2
                elif isinstance(op_node, ast.Mod):
                    return 2
                elif isinstance(op_node, ast.Pow):
                    return 3
                elif isinstance(op_node, ast.UAdd):
                    return 4
                elif isinstance(op_node, ast.USub):
                    return 4
                elif isinstance(op_node, ast.Invert):
                    return 4
                else:
                    return 0

            def traverse(node):
                if isinstance(node, ast.Expression):
                    return traverse(node.body)
                elif isinstance(node, ast.BinOp):
                    left = traverse(node.left)
                    right = traverse(node.right)
                    op_type = type(node.op).__name__
                    prec = get_precedence(node.op)
                    return {'op': op_type, 'prec': prec, 'left': left, 'right': right, 'expr': expr}
                elif isinstance(node, ast.Constant):
                    return {'val': node.value}
                elif isinstance(node, ast.Name):
                    return {'name': node.id}
                else:
                    return {'type': type(node).__name__}
            results.append((expr, result, ast.dump(tree)))
        except Exception as e:
            results.append((expr, None, str(e)))
    return results
if __name__ == '__main__':
    expressions = ['2 + 3 * 4', '(2 + 3) * 4', '10 / 2 + 3', '10 + 2 / 3', '2 ** 3 ** 2', '10 - 5 - 2']
    output = evaluate_expressions(expressions)
    for expr, res, dump in output:
        print(f'Expression: {expr}')
        print(f'Result: {res}')
        print(f'AST Dump: {dump}')
        print('-' * 20)