class LogicChecker:
    def __init__(self):
        self._valid_operators = {'and', 'or', 'not', '==', '!=', '>', '<', '>=', '<='}

    def is_valid_boolean_expression(self, expression: str) -> bool:
        tokens = expression.split()
        if len(tokens) % 2 == 0 or not tokens[0].lower() in {'true', 'false'}:
            return False

        stack = []
        for token in tokens:
            if token.lower() in self._valid_operators:
                if not stack or len(stack) < 2:
                    return False
            elif not token.isalpha() and not (token[0] == '-' and token[1:].isdigit()):
                return False
            stack.append(token)
        return len(stack) == 1

    def evaluate_expression(self, expression: str) -> bool:
        if not self.is_valid_boolean_expression(expression):
            raise ValueError("Invalid boolean expression")

        def eval_rec(tokens):
            if len(tokens) == 3:
                operator = tokens[1].lower()
                left = eval_rec([tokens[0]])
                right = eval_rec([tokens[2]])
                return {'and': left and right, 'or': left or right, '>': left > right, '<': left < right, 
                        '>=': left >= right, '<=': left <= right, '==': left == right, '!=': left != right}[operator]
            elif tokens[0].lower() in {'true', 'false'}:
                return True if tokens[0] == 'True' else False
            else:
                return int(tokens[0])

        expression = expression.replace('and', ' and ').replace('or', ' or ')
        tokens = expression.split()
        return eval_rec(tokens)

if __name__ == '__main__':
    checker = LogicChecker()
    print(checker.evaluate_expression("True and False"))
    print(checker.evaluate_expression("not True"))
    print(checker.evaluate_expression("5 > 3"))