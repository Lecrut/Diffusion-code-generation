import ast
import operator
def evaluate_boolean_expression(expression, context=None):
    if context is None:
        context = {}
    class Context:
        def __init__(self, context):
            self.context = context
    class ExpressionEvaluator(ast.NodeVisitor):
        def visit_Expression(self, node):
            if isinstance(node, ast.BoolOp):
                op = node.op
                values = [self.visit(v) for v in node.values]
                if op == "and":
                    return all(values)
                elif op == "or":
                    return any(values)
            elif isinstance(node, ast.UnaryOp):
                op = node.op
                operand = self.visit(node.operand)
                if op == "not":
                    return not operand
            elif isinstance(node, ast.Compare):
                left = self.visit(node.left)
                op = None
                right = self.visit(node.comparators[0])
                if len(node.comparators) == 1:
                    op = type(node.comparators[0])
                    right = node.comparators[0]
                elif len(node.comparators) > 1:
                    op = type(node.comparators[0])
                    right = node.comparators[0]
                if op is not None:
                    try:
                        result = operator.gt(left, right) if op == ast.Gt else \
                                  operator.lt(left, right) if op == ast.Lt else \
                                  operator.eq(left, right) if op == ast.Eq else \
                                  operator.ge(left, right) if op == ast.Ge else \
                                  operator.le(left, right) if op == ast.Le else \
                                  None
                        return bool(result)
                    except TypeError:
                        return False
                return False
            return None
    try:
        tree = ast.parse(expression, mode='eval')
        evaluator = ExpressionEvaluator()
        result = evaluator.visit(tree.body)
        return bool(result)
    except SyntaxError:
        return "Syntax Error"
    except Exception:
        return "Evaluation Error"
if __name__ == '__main__':
    def safe_eval(expr, ctx):
        try:
            return evaluate_boolean_expression(expr, ctx)
        except Exception as e:
            return f"Error: {e}"
    expr1 = "True and (5 > 3 or 1 == 1)"
    ctx1 = {"a": 5, "b": 1}
    print(f"Expression: {expr1}")
    print(f"Context: {ctx1}")
    print(f"Result: {safe_eval(expr1, ctx1)}\n")
    expr2 = "not (a == 5) or (b > 10)"
    ctx2 = {"a": 5, "b": 12}
    print(f"Expression: {expr2}")
    print(f"Context: {ctx2}")
    print(f"Result: {safe_eval(expr2, ctx2)}\n")
    expr3 = "(10 > 5) and (20 == 20) or (3 < 1)"
    ctx3 = {}
    print(f"Expression: {expr3}")
    print(f"Context: {ctx3}")
    print(f"Result: {safe_eval(expr3, ctx3)}\n")
    expr4 = "True and 5 >"
    ctx4 = {}
    print(f"Expression: {expr4}")
    print(f"Context: {ctx4}")
    print(f"Result: {safe_eval(expr4, ctx4)}\n")
    expr5 = "a == 5"
    ctx5 = {}
    print(f"Expression: {expr5}")
    print(f"Context: {ctx5}")
    print(f"Result: {safe_eval(expr5, ctx5)}\n")