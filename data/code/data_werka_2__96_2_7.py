import ast
import operator

def evaluate_boolean_expression(expression: str, variables: dict) -> bool:
    try:
        tree = ast.parse(expression, mode='eval')
    except SyntaxError as e:
        raise ValueError(f"Invalid expression syntax: {e}")

    def _eval_node(node):
        if isinstance(node, ast.Constant):
            return node.value
        if isinstance(node, ast.Name):
            name = node.id
            if name not in variables:
                raise ValueError(f"Undefined variable: {name}")
            val = variables[name]
            if not isinstance(val, bool):
                raise ValueError(f"Variable {name} must be a boolean, got {type(val).__name__}")
            return val
        if isinstance(node, ast.BoolOp):
            op_type = type(node.op)
            values = [_eval_node(v) for v in node.values]
            if op_type == ast.And:
                return all(values)
            if op_type == ast.Or:
                return any(values)
        if isinstance(node, ast.UnaryOp):
            op_type = type(node.op)
            operand = _eval_node(node.operand)
            if op_type == ast.Not:
                return not operand
        if isinstance(node, ast.Compare):
            left = _eval_node(node.left)
            comparators = [_eval_node(c) for c in node.comparators]
            ops = node.ops
            result = True
            for i, op in enumerate(ops):
                right = comparators[i]
                if isinstance(op, ast.Eq):
                    res = left == right
                elif isinstance(op, ast.NotEq):
                    res = left != right
                elif isinstance(op, ast.Lt):
                    res = left < right
                elif isinstance(op, ast.LtE):
                    res = left <= right
                elif isinstance(op, ast.Gt):
                    res = left > right
                elif isinstance(op, ast.GtE):
                    res = left >= right
                else:
                    raise ValueError(f"Unsupported operator: {op}")
                result = result and res
                left = right
            return result
        if isinstance(node, ast.BinOp):
            left = _eval_node(node.left)
            right = _eval_node(node.right)
            op_type = type(node.op)
            if op_type == ast.Add:
                return left + right
            if op_type == ast.Sub:
                return left - right
            if op_type == ast.Mult:
                return left * right
            if op_type == ast.Div:
                return left / right
            if op_type == ast.Pow:
                return left ** right
            if op_type == ast.Mod:
                return left % right
            if op_type == ast.BitXor:
                return left ^ right
            if op_type == ast.BitOr:
                return left | right
            if op_type == ast.BitAnd:
                return left & right
            if op_type == ast.LShift:
                return left << right
            if op_type == ast.RShift:
                return left >> right
            if op_type == ast.FloorDiv:
                return left // right
            if op_type == ast.MatMult:
                return left @ right
        raise ValueError(f"Unsupported node type: {type(node)}")

    return _eval_node(tree.body)

if __name__ == '__main__':
    expr = '((True and False) or (True and True))'
    vars_dict = {}
    result = evaluate_boolean_expression(expr, vars_dict)
    print(result)