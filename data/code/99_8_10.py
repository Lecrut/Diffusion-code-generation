class BooleanEvaluator:
    OPERATOR_PRECEDENCE = {
        'or': 1,
        'and': 2,
        'not': 3,
    }

    def check_precedence(self, expression_string):
        tokens = self._tokenize(expression_string)
        if not tokens:
            raise ValueError("Empty expression")
        result, _ = self._parse_or(tokens, 0)
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
            elif char in ('0', '1'):
                tokens.append(('BOOL', char == '1'))
                i += 1
            elif expression_string[i:i+2] == 'or':
                tokens.append(('OP', 'or'))
                i += 2
            elif expression_string[i:i+3] == 'and':
                tokens.append(('OP', 'and'))
                i += 3
            elif expression_string[i:i+3] == 'not':
                tokens.append(('OP', 'not'))
                i += 3
            else:
                raise ValueError(f"Unexpected character: {char}")
        return tokens

    def _parse_or(self, tokens, index):
        left, index = self._parse_and(tokens, index)
        while index < len(tokens) and tokens[index][0] == 'OP' and tokens[index][1] == 'or':
            index += 1
            right, index = self._parse_and(tokens, index)
            left = left or right
        return left, index

    def _parse_and(self, tokens, index):
        left, index = self._parse_not(tokens, index)
        while index < len(tokens) and tokens[index][0] == 'OP' and tokens[index][1] == 'and':
            index += 1
            right, index = self._parse_not(tokens, index)
            left = left and right
        return left, index

    def _parse_not(self, tokens, index):
        if index < len(tokens) and tokens[index][0] == 'OP' and tokens[index][1] == 'not':
            index += 1
            value, index = self._parse_not(tokens, index)
            return not value, index
        return self._parse_primary(tokens, index)

    def _parse_primary(self, tokens, index):
        if index >= len(tokens):
            raise ValueError("Unexpected end of expression")
        token_type, token_value = tokens[index]
        if token_type == 'BOOL':
            return token_value, index + 1
        if token_type == 'LPAREN':
            index += 1
            value, index = self._parse_or(tokens, index)
            if index >= len(tokens) or tokens[index][0] != 'RPAREN':
                raise ValueError("Missing closing parenthesis")
            return value, index + 1
        raise ValueError(f"Unexpected token: {token_value}")

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    print(evaluator.check_precedence("1 and 0 or 1"))
    print(evaluator.check_precedence("not 1 and 0"))
    print(evaluator.check_precedence("(1 or 0) and 1"))
    print(evaluator.check_precedence("not not 1"))