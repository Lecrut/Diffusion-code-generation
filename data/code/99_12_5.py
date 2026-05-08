import re
class BooleanEvaluator:
    def check_precedence(self, expression_string):
        tokens = re.findall(r'(\(|\)|\btrue\b|\bfalse\b|\d+\.?\d*|\+|\-|\*|/|!|\&|\||\^)', expression_string)
        if not tokens:
            return "Error: Empty expression"
        tokens_with_types = []
        for token in tokens:
            if token in ('true', 'false'):
                tokens_with_types.append((token, 'bool'))
            elif re.match(r'^-?\d+(\.\d+)?$|[\+\-\*\/!&^\|]', token):
                tokens_with_types.append((token, 'operator'))
            elif token in ('(', ')'):
                tokens_with_types.append((token, 'paren'))
            else:
                tokens_with_types.append((token, 'unknown'))
        if not tokens_with_types:
            return "Error: Could not parse tokens"
        precedence = {
            '(': 0,
            ')': 0,
            '!': 3,
            '&': 2,
            '|': 2,
            '^': 2,
            '*': 3,
            '/': 3,
            '+': 1,
            '-': 1,
            'true': 4,
            'false': 4,
            '1': 5,
            '0': 5
        }
        evaluation_order = []
        output_queue = []
        operator_stack = []
        for token, token_type in tokens_with_types:
            if token_type == 'bool':
                output_queue.append(token)
            elif token_type == 'paren':
                if token == '(':
                    operator_stack.append(token)
                elif token == ')':
                    while operator_stack and operator_stack[-1] != '(':
                        output_queue.append(operator_stack.pop())
                    if operator_stack and operator_stack[-1] == '(':
                        operator_stack.pop()
                else:
                    output_queue.append(token)
            elif token_type == 'operator':
                prec = precedence.get(token, 0)
                while (operator_stack and operator_stack[-1] != '(' and 
                       precedence.get(operator_stack[-1], -1) >= prec):
                    output_queue.append(operator_stack.pop())
                operator_stack.append(token)
        while operator_stack:
            output_queue.append(operator_stack.pop())
        return output_queue
if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    test_cases = [
        ("true && false || true", "True, False, True, ||, &&"),
        ("(true || false) && true", "true, false, ||, true, &&"),
        ("true && !false", "true, !, false, &&"),
        ("1 + 2 * 3", "1, 2, *, 3, +"),
        ("true | 1 && 0", "true, 1, 0, &&, |"),
        ("!(true && false)", "!, true, &&, false"),
        ("true && true && true", "true, true, true, &&, true, &&"),
        ("10 / 2 + 1", "10, 2, /, 1, +"),
        ("true && (false || true)", "true, (, false, ||, true, ), &&"),
    ]
    for expression, expected_order_hint in test_cases:
        result = evaluator.check_precedence(expression)
        print(f"Expression: '{expression}'")
        print(f"Evaluation Order (Precedence Flow): {result}")
        print("-" * 20)
    print("\n--- Complex Scenario Test ---")
    complex_expression = "true && (10 / 2) || !false"
    result = evaluator.check_precedence(complex_expression)
    print(f"Expression: '{complex_expression}'")
    print(f"Evaluation Order (Precedence Flow): {result}")