class BooleanEvaluator:
    TRUE = True
    FALSE = False

    @staticmethod
    def is_valid_token(token):
        return token in {BooleanEvaluator.TRUE, BooleanEvaluator.FALSE}

    @classmethod
    def evaluate_expression(cls, expression: str) -> bool:
        stack = []
        current_number = ''
        for char in expression:
            if char == '(':
                stack.append(char)
            elif char.isdigit():
                current_number += char
            elif char == ')':
                if current_number:
                    number = int(current_number)
                    current_number = ''
                    while stack and stack[-1] != '(':
                        number += stack.pop()
                    stack.pop()
                    stack.append(number)
                else:
                    stack.pop()
            elif char == ' ':
                continue
            else:
                raise ValueError(f'Invalid character: {char}')
        while len(stack) > 1:
            right = stack.pop()
            operator = stack.pop()
            left = stack.pop()
            if operator == '&':
                result = cls.TRUE if left and right else cls.FALSE
            elif operator == '|':
                result = cls.TRUE if left or right else cls.FALSE
            else:
                raise ValueError(f'Invalid operator: {operator}')
            stack.append(result)
        return stack[0] == cls.TRUE
if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    sample_expression = '(1 & 0) | (1 & 1)'
    print(evaluator.evaluate_expression(sample_expression))