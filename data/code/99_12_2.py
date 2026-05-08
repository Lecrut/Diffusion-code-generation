import re
class BooleanEvaluator:
    def check_precedence(self, expression_string):
        tokens = re.findall(r'\(|\)|\+|\-|\*|\/|\btrue\b|\bfalse\b|\bAND\b|\bOR\b|\bNOT\b|\b\d+\.\d+|\d+', expression_string.replace(' ', ''))
        if not tokens:
            return "Error: Empty expression"
        processed_expression = expression_string
        processed_expression = processed_expression.replace('AND', 'and').replace('OR', 'or').replace('NOT', 'not')
        try:
            result = eval(processed_expression, {"__builtins__": None}, {})
            evaluation_order = []
            if 'not' in processed_expression:
                evaluation_order.append("NOT (Highest Precedence)")
            if 'and' in processed_expression:
                evaluation_order.append("AND (Medium Precedence)")
            if 'or' in processed_expression:
                evaluation_order.append("OR (Lowest Precedence)")
            if '(' in processed_expression or ')' in processed_expression:
                evaluation_order.append("Grouping (Parentheses dictate order)")
            if not evaluation_order:
                evaluation_order.append("Simple evaluation (no complex operators)")
            return "Evaluation Order: " + " -> ".join(evaluation_order)
        except Exception as e:
            return f"Error during evaluation: {e}"
if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    test_cases = [
        ("true AND false OR true", "Test 1: Basic AND/OR"),
        ("(true OR false) AND true", "Test 2: Parentheses override"),
        ("NOT true OR false", "Test 3: NOT precedence"),
        ("true OR true OR true", "Test 4: Redundant OR"),
        ("NOT (true AND false)", "Test 5: Nested NOT"),
        ("true OR false AND true", "Test 6: AND before OR"),
        ("NOT true AND false OR true", "Test 7: Complex mix"),
        ("true AND true AND true", "Test 8: Pure AND"),
        ("false OR false OR false", "Test 9: Pure OR"),
    ]
    for expression, description in test_cases:
        result = evaluator.check_precedence(expression)
        print(f"Expression: '{expression}' ({description})")
        print(f"Result: {result}\n")