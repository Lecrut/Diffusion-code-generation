import ast
import operator
def evaluate_boolean_expression(expression, variables):
    node_map = {
        ast.And: operator.and_,
        ast.Or: operator.or_,
        ast.Not: operator.not_,
        ast.Eq: operator.eq,
        ast.NotEq: operator.ne,
        ast.Gt: operator.gt,
        ast.Lt: operator.lt,
        ast.GtE: operator.ge,
        ast.LtE: operator.le,
    }
    def _eval_node(node):
        if isinstance(node, ast.Expression):
            return _eval_node(node.body)
        elif isinstance(node, ast.Constant):
            if isinstance(node.value, bool):
                return node.value
            elif isinstance(node.value, (int, float)):
                return variables.get(node.value, 0)
            else:
                raise TypeError(f"Unsupported constant type: {type(node.value)}")
        elif isinstance(node, ast.Name):
            if node.id in variables:
                return variables[node.id]
            else:
                raise NameError(f"Variable '{node.id}' not defined")
        elif isinstance(node, ast.BoolOp):
            op = node.op
            if isinstance(op, ast.And):
                results = [_eval_node(n) for n in node.values]
                return operator.and_(*results)
            elif isinstance(op, ast.Or):
                results = [_eval_node(n) for n in node.values]
                return operator.or_(*results)
        elif isinstance(node, ast.UnaryOp):
            op = node.op
            operand = _eval_node(node.operand)
            if op == ast.Not:
                return operator.not_(operand)
        elif isinstance(node, ast.Compare):
            left = _eval_node(node.left)
            op_type = None
            right = _eval_node(node.comparators[0])
            if len(node.comparators) == 1:
                op_type = type(node.ops[0])
                if op_type in node_map:
                    op_func = node_map[op_type]
                    return op_func(left, right)
            raise ValueError("Complex comparison structure not fully supported in this simplified evaluator.")
        else:
            raise TypeError(f"Unsupported AST node type: {type(node)}")
    try:
        body = ast.parse(expression, mode='eval')
        result = _eval_node(body.body)
        return result
    except (SyntaxError, TypeError, NameError, ValueError) as e:
        return f"Error: {e}"
if __name__ == '__main__':
    variables = {
        "A": True,
        "B": False,
        "C": 10,
        "D": 5,
        "E": 20
    }
    expressions = [
        "A and not B",
        "A or B",
        "not A",
        "C > D",
        "E == 20",
        "(A and B) or not C",
        "A and (C > D or E == 20)",
        "not (A or B)",
        "A == B",
        "A > C and not D"
    ]
    print("--- Evaluation Results ---")
    for expr in expressions:
        result = evaluate_boolean_expression(expr, variables)
        print(f"Expression: '{expr}' -> Result: {result}")
    print("\n--- Error Handling Tests ---")
    error_expressions = [
        "A and $B",
        "A == B and",
        "A == 10 and",
        "A == B and C"
    ]
    for expr in error_expressions:
        result = evaluate_boolean_expression(expr, variables)
        print(f"Expression: '{expr}' -> Result: {result}")