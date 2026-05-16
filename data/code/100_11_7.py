class LogicChecker:
    def evaluate(self, expression: str, variables: dict) -> bool:
        import re
        def substitute(match):
            var_name = match.group(1)
            if var_name in variables:
                return str(variables[var_name])
            return match.group(0)
        tokens = re.findall(r'([a-zA-Z0-9_]+|\(|\)|\+|\-|\*|\/|==|!=|<=|>=|&&|\|\|)', expression)
        allowed_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789()&|!+*/=<>\"' "
        if not all(c in allowed_chars for c in expression):
            raise ValueError("Expression contains disallowed characters.")
        scope = variables.copy()
        try:
            result = eval(expression, {"__builtins__": None}, scope)
            return bool(result)
        except Exception as e:
            print(f"Evaluation error: {e}")
            return False
if __name__ == '__main__':
    checker = LogicChecker()
    vars1 = {"A": True, "B": False}
    expr1 = "A && !B"
    result1 = checker.evaluate(expr1, vars1)
    print(f"Expression: '{expr1}', Variables: {vars1} -> Result: {result1}")
    vars2 = {"X": 10, "Y": 5}
    expr2 = "(X > 5) || (Y == 5)"
    result2 = checker.evaluate(expr2, vars2)
    print(f"Expression: '{expr2}', Variables: {vars2} -> Result: {result2}")
    vars3 = {"P": False, "Q": True}
    expr3 = "P || Q"
    result3 = checker.evaluate(expr3, vars3)
    print(f"Expression: '{expr3}', Variables: {vars3} -> Result: {result3}")
    vars4 = {"R": True}
    expr4 = "R"
    result4 = checker.evaluate(expr4, vars4)
    print(f"Expression: '{expr4}', Variables: {vars4} -> Result: {result4}")
    vars5 = {"A": 1}
    expr5 = "A / 0"
    result5 = checker.evaluate(expr5, vars5)
    print(f"Expression: '{expr5}', Variables: {vars5} -> Result: {result5}")
    vars6 = {"L": True, "M": False}
    expr6 = "(L && M) || (not M)"
    vars6_safe = {"L": True, "M": False}
    expr6_safe = "(L and M) or (not M)"                                                                                                        
    result6 = checker.evaluate("L and not M", vars6_safe)
    print(f"Expression: 'L and not M', Variables: {vars6_safe} -> Result: {result6}")