import re
class BooleanEvaluator:
    def check_precedence(self, expression_string):
        tokens = re.findall(r'[\d\.\+\-\*\/\(\)\s]+|true|false', expression_string)
        if not tokens:
            return "Error: Empty expression"
        tokens = [t.strip() for t in tokens if t.strip()]
        if not tokens:
            return "Error: No valid tokens found"
        try:
            result = eval(expression_string)
            precedence_order = [
                "1. Parentheses ()",
                "2. Unary Operators (not, not None)",
                "3. Multiplication (*), Division (/), Modulo (%)",
                "4. Addition (+), Subtraction (-)",
                "5. Comparison operators (==, >, <, etc.)",
                "6. Logical NOT (not)",
                "7. Logical AND (and)",
                "8. Logical OR (or)"
            ]
            return {
                "evaluation_result": result,
                "precedence_order_followed": precedence_order,
                "notes": "Evaluation followed standard Python operator precedence rules."
            }
        except Exception as e:
            return f"Error during evaluation: {e}"
if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    test_cases = [
        ("true and false or true", "Complex logical operation"),
        ("true and false or true", "Standard precedence check"),
        ("(true or false) and true", "Parentheses override"),
        ("true and false", "Multiplication/AND first"),
        ("true or false and true", "Addition/OR precedence"),
        ("not true and false", "Negation precedence"),
        ("true and (false or true)", "Parentheses grouping"),
        ("10 + 5 * 2", "Arithmetic precedence"),
        ("3 + 4 * 2", "Arithmetic precedence"),
        ("not (true and false)", "Nested precedence"),
        ("false or 0", "Boolean/Numeric evaluation")
    ]
    for expression, description in test_cases:
        print("=" * 50)
        print(f"Expression: {expression} ({description})")
        result = evaluator.check_precedence(expression)
        if isinstance(result, dict):
            print("Evaluation Result:")
            print(f"  Result: {result['evaluation_result']}")
            print(f"  Precedence Order Used: {result['precedence_order_followed']}")
            print(f"  Notes: {result['notes']}")
        else:
            print(f"Error: {result}")
        print("=" * 50)