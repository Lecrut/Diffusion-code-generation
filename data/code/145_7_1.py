class BooleanExpression:
    def __init__(self, expression):
        self.expression = expression
    def evaluate(self, variables):
        if not self.expression:
            return False
        tokens = self.expression.split()
        result_stack = []
        for token in tokens:
            if token in variables:
                result_stack.append(variables[token])
            elif token == 'AND':
                if len(result_stack) < 2:
                    raise ValueError("Invalid AND operation: insufficient operands")
                op2 = result_stack.pop()
                op1 = result_stack.pop()
                result_stack.append(op1 and op2)
            elif token == 'OR':
                if len(result_stack) < 2:
                    raise ValueError("Invalid OR operation: insufficient operands")
                op2 = result_stack.pop()
                op1 = result_stack.pop()
                result_stack.append(op1 or op2)
            else:
                try:
                    value = bool(token)
                    result_stack.append(value)
                except ValueError:
                    raise ValueError(f"Invalid token encountered: {token}")
        if len(result_stack) != 1:
            raise ValueError("Invalid expression structure")
        return result_stack[0]
class TestFramework:
    def run_tests(self, expressions, variable_sets):
        results = {}
        for expr, vars_name in zip(expressions, variable_sets):
            try:
                result = expr.evaluate(vars_name)
                results[vars_name] = result
            except Exception as e:
                results[vars_name] = f"ERROR: {e}"
        return results
if __name__ == '__main__':
    framework = TestFramework()
    expressions = [
        "A AND B",
        "(A OR B) AND C",
        "NOT A OR B",
        "A AND (B OR C)",
        "NOT (A AND B)",
        "A OR (B AND C)"
    ]
    variable_sets = [
        {'A': True, 'B': True, 'C': False},
        {'A': True, 'B': False, 'C': True},
        {'A': False, 'B': False, 'C': False}
    ]
    print("--- Running Test Framework ---")
    all_results = {}
    for i, vars_set in enumerate(variable_sets):
        print(f"\nTesting with Variables Set {i+1}: {vars_set}")
        results = framework.run_tests(expressions, vars_set)
        all_results[f"Set {i+1}"] = results
    print("\n--- Final Results Summary ---")
    import json
    print(json.dumps(all_results, indent=4))