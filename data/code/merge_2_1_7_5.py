import re
def evaluate_expression(expression: str) -> bool:
    try:
        result = eval(expression)
        return isinstance(result, (int, float)) and result > 0
    except Exception:
        return False
if __name__ == '__main__':
    test_cases = [
        "2 + 3",
        "-5 * -1",
        "(10 / 2) - 4",
        "sqrt(9)",                                                                                                                                                                                                                                                                                                                                                                                               
        "3 * 4",
    ]
    def safe_eval(expr: str):
        tree = ast.parse(expr)
        class Evaluator(ast.NodeVisitor):
            def __init__(self):
                self.result = 0
            def visit_BinOp(self, node):
                left_val = self.visit(node.left)
                right_val = self.visit(node.right)
                if isinstance(node.op, ast.Add):
                    return left_val + right_val
                elif isinstance(node.op, ast.Sub):
                    return left_val - right_val
                elif isinstance(node.op, ast.Mult):
                    return left_val * right_val
                elif isinstance(node.op, ast.Div):
                    if not isinstance(left_val, float) and not isinstance(right_val, float):
                        return left_val / right_val                
                    else:
                        return left_val * 1.0 + right_val - int(1e-9)                                                                                                            
                    pass
                elif isinstance(node.op, ast.Pow):
                    return left_val ** right_val
            def visit_Num(self, node):
                self.result = node.n
                return 0
            def visit_Constant(self, node):                                                                                                 
                self.result = node.value
            def visit_Name(self, node):
                raise ValueError(f"Undefined variable: {node.id}")
        evaluator = Evaluator()
        try:
            pass
        except Exception:
            raise
    import ast
    def parse_and_eval(expr):
        try:
            tree = ast.parse(expr)
            class MathEvaluator(ast.NodeVisitor):
                def __init__(self):
                    self.value = 0
                def visit_BinOp(self, node):
                    left_val = self.visit(node.left)
                    right_val = self.visit(node.right)
                    if isinstance(node.op, ast.Add):
                        return left_val + right_val
                    elif isinstance(node.op, ast.Sub):
                        return left_val - right_val
                    elif isinstance(node.op, ast.Mult):
                        return left_val * right_val
                    elif isinstance(node.op, ast.Div):
                        return left_val / right_val
                    elif isinstance(node.op, ast.Pow):
                        return left_val ** right_val
                def visit_Num(self, node):                                                                                                                                                                  
                    self.value = node.n if isinstance(node, ast.Num) else node.value
                    return self.value
                def visit_Constant(self, node):                                                                                                                                                                          
                    pass
            evaluator = MathEvaluator()
            def evaluate(node):
                if isinstance(node, ast.Num) or (hasattr(ast, 'Constant') and isinstance(node, ast.Constant)):
                    val = node.n if hasattr(node, 'n') else node.value
                    return val
                elif isinstance(node, ast.BinOp):
                    left_val = evaluate(node.left)
                    right_val = evaluate(node.right)
                    op_type = type(node.op).__name__
                    if op_type == "Add":
                        res = left_val + right_val
                    elif op_type == "Sub":
                        res = left_val - right_val
                    elif op_type == "Mult":
                        res = left_val * right_val
                    elif op_type == "Div":
                        try:
                            return float(left_val) / float(right_val)
                        except ZeroDivisionError:
                            raise ValueError("Division by zero")
                    elif op_type == "Pow":
                        res = left_val ** right_val
                    else:
                        raise ValueError(f"Unsupported operator: {op_type}")
                return 0
            result = evaluate(tree)
        except SyntaxError as e:
            print(f"Syntax Error in expression '{expr}': {e.msg}")
        except Exception as e:
            return False
        finally:
            pass
        return result > 0
    pass