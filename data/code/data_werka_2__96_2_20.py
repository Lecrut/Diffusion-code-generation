import ast
import operator

def evaluate_boolean_expression(expression: str, variables: dict) -> bool:
    expression = expression.replace(' and ', ' & ')
    expression = expression.replace(' or ', ' | ')
    expression = expression.replace(' not ', ' ~ ')
    
    class BooleanTransformer(ast.NodeTransformer):
        def visit_BinOp(self, node):
            if isinstance(node.op, ast.BitAnd):
                left = self.visit(node.left)
                right = self.visit(node.right)
                return ast.Constant(value=bool(left) and bool(right))
            if isinstance(node.op, ast.BitOr):
                left = self.visit(node.left)
                right = self.visit(node.right)
                return ast.Constant(value=bool(left) or bool(right))
            return node

        def visit_UnaryOp(self, node):
            if isinstance(node.op, ast.Invert):
                operand = self.visit(node.operand)
                return ast.Constant(value=not bool(operand))
            return node

        def visit_Name(self, node):
            if node.id in variables:
                val = variables[node.id]
                if not isinstance(val, bool):
                    raise ValueError(f"Variable {node.id} must be boolean")
                return ast.Constant(value=val)
            raise ValueError(f"Undefined variable: {node.id}")

    tree = ast.parse(expression, mode='eval')
    tree = BooleanTransformer().visit(tree)
    ast.fix_missing_locations(tree)
    
    code = compile(tree, '<string>', 'eval')
    return bool(eval(code))

if __name__ == '__main__':
    expr = '((A and B) or C)'
    vars = {'A': True, 'B': False, 'C': True}
    result = evaluate_boolean_expression(expr, vars)
    print(result)