class BooleanEvaluator:
    PRECEDENCE = {'or': 1, 'and': 2, 'not': 3}
    OPERATORS = {'or', 'and', 'not'}
    OPERATOR_MAP = {'or': lambda x, y: x or y, 'and': lambda x, y: x and y, 'not': lambda x: not x}

    def check_precedence(self, expression_string):
        tokens = self._tokenize(expression_string)
        if not tokens:
            raise ValueError("Empty expression")
        result, _ = self._parse_expression(tokens, 0)
        if _ < len(tokens):
            raise ValueError("Unexpected tokens at end")
        return result

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
            elif char in ('0', '1', 'True', 'False', 'true', 'false'):
                if char in ('1', 'True', 'true'):
                    tokens.append(('BOOL', True))
                else:
                    tokens.append(('BOOL', False))
                i += 1
            elif char.isalpha():
                start = i
                while i < length and (expression_string[i].isalnum() or expression_string[i] == '_'):
                    i += 1
                word = expression_string[start:i]
                if word in self.OPERATORS:
                    tokens.append(('OP', word))
                else:
                    raise ValueError(f"Unknown identifier: {word}")
            else:
                raise ValueError(f"Unexpected character: {char}")
        return tokens

    def _parse_expression(self, tokens, index):
        left, index = self._parse_and(tokens, index)
        while index < len(tokens) and tokens[index][0] == 'OP' and tokens[index][1] == 'or':
            op = tokens[index][1]
            index += 1
            right, index = self._parse_and(tokens, index)
            left = self.OPERATOR_MAP[op](left, right)
        return left, index

    def _parse_and(self, tokens, index):
        left, index = self._parse_not(tokens, index)
        while index < len(tokens) and tokens[index][0] == 'OP' and tokens[index][1] == 'and':
            op = tokens[index][1]
            index += 1
            right, index = self._parse_not(tokens, index)
            left = self.OPERATOR_MAP[op](left, right)
        return left, index

    def _parse_not(self, tokens, index):
        if index < len(tokens) and tokens[index][0] == 'OP' and tokens[index][1] == 'not':
            index += 1
            operand, index = self._parse_not(tokens, index)
            return not operand, index
        return self._parse_primary(tokens, index)

    def _parse_primary(self, tokens, index):
        if index >= len(tokens):
            raise ValueError("Unexpected end of expression")
        token_type, token_val = tokens[index]
        if token_type == 'BOOL':
            return token_val, index + 1
        elif token_type == 'LPAREN':
            result, index = self._parse_expression(tokens, index + 1)
            if index >= len(tokens) or tokens[index][0] != 'RPAREN':
                raise ValueError("Missing closing parenthesis")
            return result, index + 1
        else:
            raise ValueError(f"Unexpected token: {token_val}")

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    print(evaluator.check_precedence("True and False or True"))
    print(evaluator.check_precedence("not True and False"))
    print(evaluator.check_precedence("(True or False) and True"))