import ast
import operator
def evaluate_boolean_expression(expression, context=None):
    if context is None:
        context = {}
    class CustomNode(ast.AST):
        pass
    def _eval_node(node, context):
        if isinstance(node, ast.Expression):
            return _eval_node(node.body, context)
        elif isinstance(node, ast.Constant):
            if isinstance(node.value, bool):
                return node.value
            elif isinstance(node.value, (int, float)):
                return node.value
            elif isinstance(node.value, str):
                return node.value
        elif isinstance(node, ast.Name):
            if node.id in context:
                return context[node.id]
            else:
                raise NameError(f"Variable '{node.id}' not defined in context.")
        elif isinstance(node, ast.BoolOp):
            op = node.op
            if isinstance(op, ast.And):
                results = [_eval_node(n, context) for n in node.values]
                return all(results)
            elif isinstance(op, ast.Or):
                results = [_eval_node(n, context) for n in node.values]
                return any(results)
            elif isinstance(op, ast.Not):
                operand = _eval_node(node.op, context)
                return not operand
        elif isinstance(node, ast.UnaryOp):
            op = node.op
            operand = _eval_node(node.operand, context)
            if op == ast.Not:
                return not operand
            elif op == ast.NotNone:
                raise TypeError("Invalid unary operator.")
        elif isinstance(node, ast.Compare):
            left = _eval_node(node.left, context)
            op = None
            right = _eval_node(node.comparators[0], context)
            if len(node.comparators) == 1:
                op = type(node.comparators[0])
                right = node.comparators[0]
            elif len(node.comparators) > 1:
                for i in range(len(node.comparators) - 1):
                    current_op = type(node.comparators[i])
                    next_comp = node.comparators[i+1]
                    if not isinstance(next_comp, ast.Compare):
                        raise TypeError("Chained comparisons must be of the same type.")
                    if not isinstance(next_comp.comparators[0], type(node.comparators[i])):
                        raise TypeError("Chained comparison types must match.")
                    node.comparators = [node.comparators[i]] + next_comp.comparators
                    op = type(node.comparators[i])
                    right = node.comparators[i+1]
                op = type(node.comparators[0])
                right = node.comparators[-1]
            if op:
                if op == ast.Eq: return left == right
                if op == ast.NotEq: return left != right
                if op == ast.Gt: return left > right
                if op == ast.Lt: return left < right
                if op == ast.GtE: return left >= right
                if op == ast.LtE: return left <= right
                if op == ast.Is: return left is right
                if op == ast.IsNot: return left is not right
                if op == ast.In: return right in left
                if op == ast.NotIn: return right not in left
            else:
                raise ValueError("Invalid comparison structure.")
        else:
            raise TypeError(f"Unsupported AST node type: {type(node)}")
    try:
        return _eval_node(ast.parse(expression, mode='eval'), context)
    except Exception as e:
        raise SyntaxError(f"Error evaluating expression: {e}")
if __name__ == '__main__':
    data = {
        "A": True,
        "B": False,
        "C": 10,
        "D": 20,
        "is_valid": True
    }
    expression1 = "(A and not B) or (C > 5)"
    try:
        result1 = evaluate_boolean_expression(expression1, data)
        print(f"Expression: {expression1}")
        print(f"Result 1: {result1}")
    except Exception as e:
        print(f"Error in Example 1: {e}")
    print("-" * 20)
    expression2 = "D >= 15 and A == True"
    try:
        result2 = evaluate_boolean_expression(expression2, data)
        print(f"Expression: {expression2}")
        print(f"Result 2: {result2}")
    except Exception as e:
        print(f"Error in Example 2: {e}")
    print("-" * 20)
    expression3 = "not (B or C == 10)"
    try:
        result3 = evaluate_boolean_expression(expression3, data)
        print(f"Expression: {expression3}")
        print(f"Result 3: {result3}")
    except Exception as e:
        print(f"Error in Example 3: {e}")
    print("-" * 20)
    expression4 = "A and B or"
    try:
        result4 = evaluate_boolean_expression(expression4, data)
        print(f"Expression: {expression4}")
        print(f"Result 4: {result4}")
    except SyntaxError as e:
        print(f"Successfully caught Syntax Error for Example 4: {e}")
    except Exception as e:
        print(f"Caught unexpected error for Example 4: {e}")