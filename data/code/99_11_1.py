import ast
import operator
def evaluate_boolean_expression(expression, context=None):
    if context is None:
        context = {}
    class CustomNode(ast.AST):
        pass
    def _eval_node(node, ctx):
        if isinstance(node, ast.Expression):
            return _eval_node(node.body, ctx)
        elif isinstance(node, ast.Constant):
            if isinstance(node.value, bool):
                return node.value
            elif isinstance(node.value, (int, float)):
                return context.get(node.value, 0)
            elif isinstance(node.value, str):
                return node.value
        elif isinstance(node, ast.Name):
            if node.id in context:
                return context[node.id]
            else:
                raise NameError(f"Variable '{node.id}' not defined in context.")
        elif isinstance(node, ast.BoolOp):
            op = node.op
            values = [_eval_node(v, ctx) for v in node.values]
            if op == "and":
                return all(values)
            elif op == "or":
                return any(values)
            elif op == "not":
                pass
            else:
                raise TypeError(f"Unsupported boolean operation: {op}")
        elif isinstance(node, ast.UnaryOp):
            op = node.op
            operand = _eval_node(node.operand, ctx)
            if op == "not":
                return not operand
            else:
                raise TypeError(f"Unsupported unary operation: {op}")
        elif isinstance(node, ast.Compare):
            left = _eval_node(node.left, ctx)
            op = None
            right = _eval_node(node.comparators[0], ctx)
            if len(node.comparators) == 1:
                op = type(node.ops[0])
                right = _eval_node(node.comparators[0], ctx)
            if op is None:
                raise ValueError("Invalid comparison structure.")
            if op == "==":
                return left == right
            elif op == "!=":
                return left != right
            elif op == ">":
                return left > right
            elif op == "<":
                return left < right
            elif op == ">=":
                return left >= right
            elif op == "<=":
                return left <= right
            elif op == "in":
                if not isinstance(right, (list, set)):
                    raise TypeError("Comparison 'in' requires a sequence on the right.")
                return right in left
            elif op == "not in":
                if not isinstance(right, (list, set)):
                    raise TypeError("Comparison 'not in' requires a sequence on the right.")
                return not (right in left)
            else:
                raise TypeError(f"Unsupported comparison operator: {op}")
        raise TypeError(f"Unknown AST node type encountered: {type(node)}")
    try:
        node = ast.parse(expression, mode='eval')
        result = _eval_node(node.body, context)
        return result
    except SyntaxError as e:
        raise ValueError(f"Syntax Error in expression: {e}")
    except NameError as e:
        raise ValueError(f"Context Error: {e}")
    except TypeError as e:
        raise ValueError(f"Evaluation Error: {e}")
    except Exception as e:
        raise ValueError(f"An unexpected error occurred during evaluation: {e}")
if __name__ == '__main__':
    context_data = {
        "A": 10,
        "B": 5,
        "C": 20,
        "is_valid": True,
        "score": 85
    }
    print("--- Test Case 1: Simple Boolean Logic (and, or, not) ---")
    expression1 = "(A > 5) and (B == 5) or not is_valid"
    try:
        result1 = evaluate_boolean_expression(expression1, context_data)
        print(f"Expression: {expression1}")
        print(f"Result: {result1}")
    except ValueError as e:
        print(f"Error: {e}")
    print("\n--- Test Case 2: Complex Comparison ---")
    expression2 = "score >= 80 and C > A"
    try:
        result2 = evaluate_boolean_expression(expression2, context_data)
        print(f"Expression: {expression2}")
        print(f"Result: {result2}")
    except ValueError as e:
        print(f"Error: {e}")
    print("\n--- Test Case 3: String and Membership Comparison ---")
    context_data_2 = {
        "items": ["apple", "banana"],
        "name": "apple"
    }
    expression3 = "name == 'apple' and 'apple' in items"
    try:
        result3 = evaluate_boolean_expression(expression3, context_data_2)
        print(f"Expression: {expression3}")
        print(f"Result: {result3}")
    except ValueError as e:
        print(f"Error: {e}")
    print("\n--- Test Case 4: Syntax Error Handling ---")
    expression4 = "A > 5 and"
    try:
        result4 = evaluate_boolean_expression(expression4, context_data)
        print(f"Expression: {expression4}")
        print(f"Result: {result4}")
    except ValueError as e:
        print(f"Error caught successfully: {e}")
    print("\n--- Test Case 5: Undefined Variable Handling ---")
    expression5 = "A > Z"
    try:
        result5 = evaluate_boolean_expression(expression5, context_data)
        print(f"Expression: {expression5}")
        print(f"Result: {result5}")
    except ValueError as e:
        print(f"Error caught successfully: {e}")