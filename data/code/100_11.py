class LogicChecker:
    def evaluate(self, expression: str, variables: dict) -> bool:
        import re
        def substitute(match):
            var_name = match.group(1)
            if var_name in variables:
                return str(variables[var_name])
            return match.group(0)
        tokens = re.findall(r'\(|\)|\w+|\+|\-|\*|\/|=', expression)
        if not tokens:
            raise ValueError("Empty expression")
        values = []
        operators = []
        for token in tokens:
            if token.replace('-', '').replace('*', '').replace('/', '') in ('+', '-', '*', '/'):
                operators.append(token)
            elif token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
                values.append(float(token))
            elif token == '(':
                values.append(0)                            
            elif token == ')':
                pass
            else:
                values.append(variables.get(token, 0))
        processed_expression = expression
        for var, val in variables.items():
            processed_expression = processed_expression.replace(var, str(val))
        try:
            result = eval(processed_expression)
            return bool(result)
        except Exception:
            return False
if __name__ == '__main__':
    checker = LogicChecker()
    expression1 = "5 + 3 * 2"
    variables1 = {"x": 10}
    result1 = checker.evaluate(expression1, variables1)
    print(f"Expression: '{expression1}', Variables: {variables1}")
    print(f"Result: {result1}")
    expression2 = "(x > 5) and (10 / 2 == 5)"
    variables2 = {"x": 7}
    result2 = checker.evaluate(expression2, variables2)
    print(f"Expression: '{expression2}', Variables: {variables2}")
    print(f"Result: {result2}")
    expression3 = "10 > x or x == 10"
    variables3 = {"x": 10}
    result3 = checker.evaluate(expression3, variables3)
    print(f"Expression: '{expression3}', Variables: {variables3}")
    print(f"Result: {result3}")
    expression4 = "x * 2 - 1"
    variables4 = {"x": 5}
    result4 = checker.evaluate(expression4, variables4)
    print(f"Expression: '{expression4}', Variables: {variables4}")
    print(f"Result: {result4}")
    expression5 = "5 / (x - 1)"
    variables5 = {"x": 5}
    result5 = checker.evaluate(expression5, variables5)
    print(f"Expression: '{expression5}', Variables: {variables5}")
    print(f"Result: {result5}")