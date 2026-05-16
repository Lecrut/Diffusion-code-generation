class LogicChecker:
    def evaluate(self, expression: str, variables: dict) -> bool:
        import re
        def substitute(match):
            var_name = match.group(1)
            if var_name in variables:
                return str(variables[var_name])
            return match.group(0)
        tokens = re.findall(r'[\w\s\+\-\*\/\(\)\=\&|]', expression)
        processed_expression = expression
        for var, value in variables.items():
            processed_expression = re.sub(r'\b' + re.escape(var) + r'\b', str(value), processed_expression)
        try:
            result = eval(processed_expression)
            return bool(result)
        except Exception:
            return False
if __name__ == '__main__':
    checker = LogicChecker()
    variables1 = {"A": True, "B": False}
    expression1 = "A AND NOT B"
    result1 = checker.evaluate(expression1, variables1)
    print(f"Expression: '{expression1}' with variables {variables1}: {result1}")
    variables2 = {"X": True, "Y": True}
    expression2 = "X OR Y"
    result2 = checker.evaluate(expression2, variables2)
    print(f"Expression: '{expression2}' with variables {variables2}: {result2}")
    variables3 = {"P": True, "Q": False}
    expression3 = "(P AND Q) OR (NOT P)"
    result3 = checker.evaluate(expression3, variables3)
    print(f"Expression: '{expression3}' with variables {variables3}: {result3}")
    variables4 = {"A": True}
    expression4 = "A AND B"
    result4 = checker.evaluate(expression4, variables4)
    print(f"Expression: '{expression4}' with variables {variables4}: {result4}")