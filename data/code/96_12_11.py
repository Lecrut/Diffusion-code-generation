class BooleanEvaluator:

    def evaluate_expression(self, expr: str) -> bool:
        stack = []
        operators = {'+', '-', '*', '/', '(', ')', '&', '|'}
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '&': 3, '|': 3}
        current_number = ''
        current_operator = '+'

        def apply_operator():
            nonlocal stack, current_number, current_operator
            left = stack.pop()
            if isinstance(left, str) and (not left.startswith('(')):
                raise SyntaxError('Syntax error')
            right = current_number
            current_number = ''
            if current_operator == '&':
                stack.append(int(left) & int(right))
            elif current_operator == '|':
                stack.append(int(left) | int(right))
        for char in expr:
            if char.isdigit():
                current_number += char
            elif char in operators:
                if char == '(':
                    stack.append(char)
                elif char == ')':
                    while stack[-1] != '(':
                        apply_operator()
                    stack.pop()
                else:
                    while stack and stack[-1] != '(' and (precedence[char] <= precedence[stack[-1]]):
                        apply_operator()
                    stack.append(char)
            if char in operators:
                current_operator = char
        while stack:
            apply_operator()
        return bool(stack[0])
if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    sample_expr = '(True & False) | True'
    print(evaluator.evaluate_expression(sample_expr))