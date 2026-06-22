class BooleanEvaluator:
    OPERATOR_PRECEDENCE = {
        'or': 1,
        'and': 2,
        'not': 3,
    }

    def check_precedence(self, expression_string):
        tokens = self._tokenize(expression_string)
        if not tokens:
            return False
        result, _ = self._parse_expression(tokens, 0)
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
            elif char in ('!', '~'):
                tokens.append(('NOT', 'not'))
                i += 1
            elif char in ('&', '|'):
                if char == '&':
                    tokens.append(('AND', 'and'))
                else:
                    tokens.append(('OR', 'or'))
                i += 1
            elif char.isalpha():
                word = char
                i += 1
                while i < length and expression_string[i].isalnum():
                    word += expression_string[i]
                    i += 1
                word_lower = word.lower()
                if word_lower == 'true':
                    tokens.append(('VALUE', True))
                elif word_lower == 'false':
                    tokens.append(('VALUE', False))
                else:
                    tokens.append(('NAME', word_lower))
            else:
                raise ValueError(f"Invalid character: {char}")
        return tokens

    def _parse_expression(self, tokens, pos):
        result, pos = self._parse_or(tokens, pos)
        return result, pos

    def _parse_or(self, tokens, pos):
        left, pos = self._parse_and(tokens, pos)
        while pos < len(tokens) and tokens[pos][1] == 'or':
            pos += 1
            right, pos = self._parse_and(tokens, pos)
            left = left or right
        return left, pos

    def _parse_and(self, tokens, pos):
        left, pos = self._parse_not(tokens, pos)
        while pos < len(tokens) and tokens[pos][1] == 'and':
            pos += 1
            right, pos = self._parse_not(tokens, pos)
            left = left and right
        return left, pos

    def _parse_not(self, tokens, pos):
        if pos < len(tokens) and tokens[pos][1] == 'not':
            pos += 1
            operand, pos = self._parse_not(tokens, pos)
            return not operand
        return self._parse_primary(tokens, pos)

    def _parse_primary(self, tokens, pos):
        if pos >= len(tokens):
            raise ValueError("Unexpected end of expression")
        token_type, token_value = tokens[pos]
        if token_type == 'VALUE':
            return token_value, pos + 1
        if token_type == 'LPAREN':
            pos += 1
            result, pos = self._parse_expression(tokens, pos)
            if pos >= len(tokens) or tokens[pos][0] != 'RPAREN':
                raise ValueError("Missing closing parenthesis")
            return result, pos + 1
        if token_type == 'NAME':
            if token_value == 'true':
                return True, pos + 1
            elif token_value == 'false':
                return False, pos + 1
            else:
                raise ValueError(f"Unknown variable: {token_value}")
        raise ValueError(f"Unexpected token: {token_value}")

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    test_cases = [
        ("true", True),
        ("false", False),
        ("true and false", False),
        ("true or false", True),
        ("not true", False),
        ("(true or false) and false", False),
        ("true or false and false", True),
        ("not (true and false)", True),
    ]
    for expr, expected in test_cases:
        result = evaluator.check_precedence(expr)
        assert result == expected, f"Failed for {expr}: expected {expected}, got {result}"
    print("All tests passed.")