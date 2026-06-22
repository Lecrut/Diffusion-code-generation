class BooleanEvaluator:
    def check_precedence(self, expression_string):
        expression_string = expression_string.strip()
        if not expression_string:
            raise ValueError("Empty expression")
        tokens = self._tokenize(expression_string)
        if not tokens:
            raise ValueError("No tokens found")
        precedence_map = {
            '(': 0,
            ')': 0,
            'or': 1,
            'and': 2,
            'not': 3,
        }
        operator_tokens = []
        operand_stack = []
        i = 0
        while i < len(tokens):
            token_type, token_value = tokens[i]
            if token_type == 'VALUE':
                operand_stack.append(token_value)
            elif token_type == 'LPAREN':
                operator_tokens.append(token_value)
            elif token_type == 'RPAREN':
                while operator_tokens and operator_tokens[-1] != '(':
                    self._apply_operator(operand_stack, operator_tokens)
                if operator_tokens and operator_tokens[-1] == '(':
                    operator_tokens.pop()
            elif token_type == 'OPERATOR':
                while (operator_tokens and
                       operator_tokens[-1] != '(' and
                       precedence_map.get(operator_tokens[-1], 0) >= precedence_map.get(token_value, 0)):
                    self._apply_operator(operand_stack, operator_tokens)
                operator_tokens.append(token_value)
            i += 1
        while operator_tokens:
            self._apply_operator(operand_stack, operator_tokens)
        if len(operand_stack) != 1:
            raise ValueError("Invalid expression")
        return operand_stack[0]

    def _tokenize(self, expression_string):
        tokens = []
        i = 0
        length = len(expression_string)
        while i < length:
            char = expression_string[i]
            if char.isspace():
                i += 1
                continue
            if char == '(':
                tokens.append(('LPAREN', '('))
                i += 1
            elif char == ')':
                tokens.append(('RPAREN', ')'))
                i += 1
            elif char in ('and', 'or', 'not'):
                start = i
                while i < length and expression_string[i].isalpha():
                    i += 1
                word = expression_string[start:i]
                if word in ('and', 'or', 'not'):
                    tokens.append(('OPERATOR', word))
                else:
                    raise ValueError(f"Unknown operator: {word}")
            elif char in ('True', 'False'):
                start = i
                while i < length and expression_string[i].isalpha():
                    i += 1
                word = expression_string[start:i]
                if word == 'True':
                    tokens.append(('VALUE', True))
                elif word == 'False':
                    tokens.append(('VALUE', False))
                else:
                    raise ValueError(f"Unknown value: {word}")
            else:
                raise ValueError(f"Unexpected character: {char}")
        return tokens

    def _apply_operator(self, operand_stack, operator_stack):
        operator = operator_stack.pop()
        if operator == 'not':
            if len(operand_stack) < 1:
                raise ValueError("Invalid expression")
            operand = operand_stack.pop()
            operand_stack.append(not operand)
        else:
            if len(operand_stack) < 2:
                raise ValueError("Invalid expression")
            right = operand_stack.pop()
            left = operand_stack.pop()
            if operator == 'and':
                operand_stack.append(left and right)
            elif operator == 'or':
                operand_stack.append(left or right)

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    print(evaluator.check_precedence("True and False or True"))
    print(evaluator.check_precedence("not True and False"))
    print(evaluator.check_precedence("(True or False) and False"))