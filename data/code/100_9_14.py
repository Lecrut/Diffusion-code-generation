import ast

class BooleanExpressionValidator:
    def is_valid_boolean_expression(self, expression):
        try:
            tree = ast.parse(expression)
            if len(tree.body) == 1 and isinstance(tree.body[0], ast.Expr):
                value = tree.body[0].value
                return isinstance(value, (ast.NameConstant, ast.UnaryOp))
            else:
                return False
        except SyntaxError:
            return False

if __name__ == '__main__':
    validator = BooleanExpressionValidator()
    print(validator.is_valid_boolean_expression("True"))
    print(validator.is_valid_boolean_expression("False"))
    print(validator.is_valid_boolean_expression("not True"))
    print(validator.is_valid_boolean_expression("and True"))
    print(validator.is_valid_boolean_expression("or False"))
    print(validator.is_valid_boolean_expression("1 + 2"))