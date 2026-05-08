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
        for var, value in variables.items():
            processed_expression = processed_expression.replace(var, str(value))
        try:
            result = eval(processed_expression)
            return bool(result)
        except Exception as e:
            raise ValueError(f"Error evaluating expression '{expression}' with variables {variables}: {e}")
if __name__ == '__main__':
    checker = LogicChecker()
    vars1 = {"A": 10, "B": 5}
    expr1 = "A > B"
    result1 = checker.evaluate(expr1, vars1)
    print(f"Expression: '{expr1}' with {vars1}: {result1}")
    vars2 = {"X": True, "Y": False}
    expr2 = "(X == True) and (Y == False)"
    result2 = checker.evaluate(expr2, vars2)
    print(f"Expression: '{expr2}' with {vars2}: {result2}")
    vars3 = {"P": 1, "Q": 0}
    expr3 = "P <= Q + 1"
    result3 = checker.evaluate(expr3, vars3)
    print(f"Expression: '{expr3}' with {vars3}: {result3}")
    try:
        vars4 = {"A": 10}
        expr4 = "A == B"                 
        checker.evaluate(expr4, vars4)
    except ValueError as e:
        print(f"Error caught for invalid expression: {e}")
    vars5 = {"A": 1, "B": 2}
    expr5 = "A == B"
    result5 = checker.evaluate(expr5, vars5)
    print(f"Expression: '{expr5}' with {vars5}: {result5}")