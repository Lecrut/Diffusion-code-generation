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
                return node.value
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
                right = node.comparators[0]
            elif len(node.comparators) > 1:
                current_op = node.ops[0]
                current_right = node.comparators[0]
                for i in range(1, len(node.comparators)):
                    next_op = node.ops[i]
                    next_right = node.comparators[i]
                    if not isinstance(next_right, (ast.Constant, ast.Name)):
                        raise TypeError("Invalid right operand in chained comparison")
                    if not isinstance(current_right, (int, float)) and not isinstance(next_right, (int, float)):
                        raise TypeError("Chained comparison requires numeric operands")
                    if not _eval_node(current_right) in (True, False):
                        raise TypeError("Chained comparison requires boolean result")
                    current_right = next_right
                    current_op = next_op
                    if current_op not in node_map:
                        raise TypeError(f"Unsupported comparison operator: {type(current_op)}")
                    current_result = node_map[current_op](_eval_node(current_right), _eval_node(current_right))
                    pass                                                                                                       
                if len(node.comparators) == 1:
                    op_type = type(node.ops[0])
                    right = node.comparators[0]
                else:
                    op_type = type(node.ops[0])
                    right = node.comparators[0]
            if op_type:
                return node_map[op_type](left, right)
            else:
                raise ValueError("Invalid comparison structure encountered")
        else:
            raise TypeError(f"Unsupported AST node type: {type(node)}")
    try:
        return _eval_node(ast.Expression(body=expression))
    except Exception as e:
        raise ValueError(f"Error during evaluation: {e}")
if __name__ == '__main__':
    variables = {
        "A": True,
        "B": False,
        "C": 10,
        "D": 5
    }
    expression1 = "(A and not B) or (C > D)"
    print(f"Expression: {expression1}")
    try:
        result1 = evaluate_boolean_expression(expression1, variables)
        print(f"Result 1: {result1}")
    except ValueError as e:
        print(f"Error 1: {e}")
    print("-" * 20)
    expression2 = "A == True and B != False"
    print(f"Expression: {expression2}")
    try:
        result2 = evaluate_boolean_expression(expression2, variables)
        print(f"Result 2: {result2}")
    except ValueError as e:
        print(f"Error 2: {e}")
    print("-" * 20)
    expression3 = "C > D and A"
    print(f"Expression: {expression3}")
    try:
        result3 = evaluate_boolean_expression(expression3, variables)
        print(f"Result 3: {result3}")
    except ValueError as e:
        print(f"Error 3: {e}")
    print("-" * 20)
    expression4 = "A + B"
    print(f"Expression: {expression4}")
    try:
        result4 = evaluate_boolean_expression(expression4, variables)
        print(f"Result 4: {result4}")
    except ValueError as e:
        print(f"Error 4 (Expected Error): {e}")
    print("-" * 20)
    expression5 = "X and A"
    print(f"Expression: {expression5}")
    try:
        result5 = evaluate_boolean_expression(expression5, variables)
        print(f"Result 5: {result5}")
    except ValueError as e:
        print(f"Error 5 (Expected Error): {e}")