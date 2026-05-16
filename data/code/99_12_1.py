import re
class BooleanEvaluator:
    def check_precedence(self, expression_string):
        tokens = re.findall(r'\(|\)|\+|\-|\*|\/|\btrue\b|\bfalse\b|\bAND\b|\bOR\b|\bNOT\b|\b\d+\.\d+|\d+', expression_string)
        if not tokens:
            return "Error: Empty expression"
        output_order = []
        operator_stack = []
        precedence = {
            'NOT': 3,
            'AND': 2,
            'OR': 1,
            '(': 0,
            ')': 0
        }
        for token in tokens:
            if token.replace('.', '', 1).isdigit() or token in ('true', 'false'):
                output_order.append(token)
            elif token in precedence:
                operator_stack.append(token)
            elif token == '(':
                operator_stack.append(token)
            elif token == ')':
                while operator_stack and operator_stack[-1] != '(':
                    output_order.append(operator_stack.pop())
                if operator_stack and operator_stack[-1] == '(':
                    operator_stack.pop()
            elif token in ('AND', 'OR', '*', '/'):
                while (operator_stack and operator_stack[-1] != '(' and 
                       precedence.get(operator_stack[-1], 0) >= precedence[token]):
                    output_order.append(operator_stack.pop())
                operator_stack.append(token)
            elif token == 'NOT':
                operator_stack.append(token)
        while operator_stack:
            output_order.append(operator_stack.pop())
        return output_order
if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    test_cases = [
        ("true AND false OR true", ["true", "false", "true", "AND", "OR"]),
        ("(true OR false) AND true", ["(", "true", "OR", "false", ")", "AND", "true"]),
        ("NOT true OR false", ["NOT", "true", "OR", "false"]),
        ("true AND (false OR true)", ["true", "AND", "(", "false", "OR", "true", ")"]),
        ("true OR false AND true", ["true", "OR", "false", "AND", "true"]),
        ("true AND true AND true", ["true", "AND", "true", "AND", "true"]),
        ("NOT (true AND false)", ["NOT", "(", "true", "AND", "false", ")"])
    ]
    for expression, expected_structure in test_cases:
        result = evaluator.check_precedence(expression)
        print(f"Expression: '{expression}'")
        print(f"Evaluation Order (Tokens/Operators): {result}")
        print("-" * 20)