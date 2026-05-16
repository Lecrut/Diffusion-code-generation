class LogicChecker:
    def evaluate(self, expression: str, variables: dict) -> bool:
        import re
        def substitute(match):
            var_name = match.group(1)
            if var_name in variables:
                return str(variables[var_name])
            return match.group(0)
        tokens = re.findall(r'([a-zA-Z0-9_]+|\(|\)|\+|\-|\*|\/|==|!=|>=|<=)', expression)
        if not tokens:
            raise ValueError("Empty expression provided")
        processed_expression = expression
        for var_name, value in variables.items():
            processed_expression = re.sub(r'\b' + re.escape(var_name) + r'\b', str(value), processed_expression)
        processed_expression = processed_expression.replace('&&', 'and').replace('||', 'or').replace('==', '==').replace('!=', '!=')
        try:
            result = eval(processed_expression)
            return bool(result)
        except Exception as e:
            raise ValueError(f"Error evaluating expression '{expression}': {e}")
if __name__ == '__main__':
    checker = LogicChecker()
    variables1 = {
        "A": True,
        "B": False,
        "C": 10
    }
    expression1 = "A and (B or not C)"
    result1 = checker.evaluate(expression1, variables1)
    print(f"Expression: '{expression1}' with variables {variables1}")
    print(f"Result: {result1}")
    variables2 = {
        "X": 5,
        "Y": 10,
        "Z": 3
    }
    expression2 = "(X > 3) and (Y <= 15)"
    result2 = checker.evaluate(expression2, variables2)
    print(f"\nExpression: '{expression2}' with variables {variables2}")
    print(f"Result: {result2}")
    variables3 = {
        "P": True,
        "Q": False
    }
    expression3 = "P != Q"
    result3 = checker.evaluate(expression3, variables3)
    print(f"\nExpression: '{expression3}' with variables {variables3}")
    print(f"Result: {result3}")
    try:
        variables4 = {"A": 1}
        expression4 = "A + B"
        checker.evaluate(expression4, variables4)
    except ValueError as e:
        print(f"\nError caught for invalid operation: {e}")