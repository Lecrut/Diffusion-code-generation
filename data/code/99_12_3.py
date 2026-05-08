import re
class BooleanEvaluator:
    def check_precedence(self, expression_string):
        tokens = re.findall(r'\(|\)|\+|\-|\*|\/|\btrue\b|\bfalse\b|\bAND\b|\bOR\b|\bNOT\b|\b\d+\.\d+|\d+', expression_string)
        if not tokens:
            return "Error: Empty expression"
        token_list = [t.strip() for t in tokens if t.strip()]
        if not token_list:
            return "Error: No valid tokens found"
        evaluation_order = []
        parentheses_level = 0
        for token in token_list:
            if token == '(':
                parentheses_level += 1
            elif token == ')':
                parentheses_level -= 1
            if parentheses_level == 0:
                evaluation_order.append(token)
        if not evaluation_order:
            return "Evaluation structure determined (requires full parsing for exact result)"
        return f"Tokens found: {token_list}\nSimulated Precedence Grouping: {evaluation_order}"
if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    test_cases = [
        ("true OR false", "Test 1: Simple OR"),
        ("(true OR false) AND true", "Test 2: Parentheses override"),
        ("true AND false OR true", "Test 3: AND before OR"),
        ("true OR true OR true", "Test 4: Left-to-right OR"),
        ("NOT true AND false", "Test 5: NOT precedence"),
        ("true AND (false OR true)", "Test 6: Nested precedence"),
        ("true OR false AND true", "Test 7: AND before OR"),
        ("true AND true AND true", "Test 8: Sequential AND"),
        ("false OR (true AND false)", "Test 9: Complex nesting")
    ]
    for expression, description in test_cases:
        result = evaluator.check_precedence(expression)
        print(f"--- {description} ---")
        print(f"Expression: {expression}")
        print(f"Result: {result}\n")