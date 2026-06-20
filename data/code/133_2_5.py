import ast

def evaluate_boolean_expression(expression: str) -> bool:
    return eval(compile(ast.parse(expression).body[0], filename="<ast>", mode="eval"))

if __name__ == '__main__':
    sample_expression = "2 + 2 == 4"
    result = evaluate_boolean_expression(sample_expression)
    print(result)