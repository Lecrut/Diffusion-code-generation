class BooleanEvaluator:
    PRECEDENCE = {
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
            elif char == 'n' and expression_string[i:i+3].lower() == 'not':
                tokens.append(('NOT', 'not'))
                i += 3
            elif char == 'a' and expression_string[i:i+3].lower() == 'and':
                tokens.append(('AND', 'and'))
                i += 3
            elif char == 'o' and expression_string[i:i+2].lower() == 'or':
                tokens.append(('OR', 'or'))
                i += 2
            elif char in '01':
                tokens.append(('BOOL', char == '1'))
                i += 1
            else:
                raise ValueError(f"Unexpected character: {char}")
        return tokens

    def _parse_or(self, tokens, pos):
        left, pos = self._parse_and(tokens, pos)
        while pos < len(tokens) and tokens[pos][0] == 'OR':
            pos += 1
            right, pos = self._parse_and(tokens, pos)
            left = left or right
        return left, pos

    def _parse_and(self, tokens, pos):
        left, pos = self._parse_not(tokens, pos)
        while pos < len(tokens) and tokens[pos][0] == 'AND':
            pos += 1
            right, pos = self._parse_not(tokens, pos)
            left = left and right
        return left, pos

    def _parse_not(self, tokens, pos):
        if pos < len(tokens) and tokens[pos][0] == 'NOT':
            pos += 1
            val, pos = self._parse_not(tokens, pos)
            return not val, pos
        return self._parse_primary(tokens, pos)

    def _parse_primary(self, tokens, pos):
        if pos >= len(tokens):
            raise ValueError("Unexpected end of expression")
        token_type, token_val = tokens[pos]
        if token_type == 'BOOL':
            return token_val, pos + 1
        if token_type == 'LPAREN':
            pos += 1
            val, pos = self._parse_or(tokens, pos)
            if pos >= len(tokens) or tokens[pos][0] != 'RPAREN':
                raise ValueError("Missing closing parenthesis")
            return val, pos + 1
        raise ValueError(f"Unexpected token: {token_val}")

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    print(evaluator.check_precedence("1 or 0 and 0"))
    print(evaluator.check_precedence("1 and 0 or 1"))
    print(evaluator.check_precedence("not 1 and 0"))
    print(evaluator.check_precedence("(1 or 0) and 0"))