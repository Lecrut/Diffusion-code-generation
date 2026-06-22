class BooleanEvaluator:
    def check_precedence(self, expression_string):
        if not expression_string or not expression_string.strip():
            raise ValueError("Empty expression")
        tokens = self._tokenize(expression_string)
        if not tokens:
            raise ValueError("No valid tokens found")
        result, _ = self._parse_or(tokens, 0)
        return result

    def _tokenize(self, expr):
        tokens = []
        i = 0
        length = len(expr)
        while i < length:
            char = expr[i]
            if char.isspace():
                i += 1
                continue
            if char == '(':
                tokens.append(('LPAREN', '('))
                i += 1
            elif char == ')':
                tokens.append(('RPAREN', ')'))
                i += 1
            elif char == '!':
                tokens.append(('NOT', 'not'))
                i += 1
            elif char == '&' and i + 1 < length and expr[i + 1] == '&':
                tokens.append(('AND', 'and'))
                i += 2
            elif char == '|' and i + 1 < length and expr[i + 1] == '|':
                tokens.append(('OR', 'or'))
                i += 2
            elif char in '01':
                tokens.append(('BOOL', char == '1'))
                i += 1
            else:
                word = []
                while i < length and expr[i].isalnum():
                    word.append(expr[i])
                    i += 1
                if word:
                    word_str = ''.join(word).lower()
                    if word_str == 'true':
                        tokens.append(('BOOL', True))
                    elif word_str == 'false':
                        tokens.append(('BOOL', False))
                    else:
                        raise ValueError(f"Unknown identifier: {word_str}")
                else:
                    raise ValueError(f"Unexpected character: {char}")
        return tokens

    def _parse_or(self, tokens, pos):
        pos, left = self._parse_and(tokens, pos)
        while pos < len(tokens) and tokens[pos][0] == 'OR':
            pos += 1
            pos, right = self._parse_and(tokens, pos)
            left = left or right
        return pos, left

    def _parse_and(self, tokens, pos):
        pos, left = self._parse_not(tokens, pos)
        while pos < len(tokens) and tokens[pos][0] == 'AND':
            pos += 1
            pos, right = self._parse_not(tokens, pos)
            left = left and right
        return pos, left

    def _parse_not(self, tokens, pos):
        if pos < len(tokens) and tokens[pos][0] == 'NOT':
            pos += 1
            pos, val = self._parse_not(tokens, pos)
            return pos, not val
        return self._parse_primary(tokens, pos)

    def _parse_primary(self, tokens, pos):
        if pos >= len(tokens):
            raise ValueError("Unexpected end of expression")
        token_type, token_val = tokens[pos]
        if token_type == 'LPAREN':
            pos += 1
            pos, val = self._parse_or(tokens, pos)
            if pos >= len(tokens) or tokens[pos][0] != 'RPAREN':
                raise ValueError("Missing closing parenthesis")
            pos += 1
            return pos, val
        elif token_type == 'BOOL':
            return pos + 1, token_val
        else:
            raise ValueError(f"Unexpected token: {token_val}")

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    test_cases = [
        ("1 or 0", True),
        ("0 and 1", False),
        ("not 1", False),
        ("(1 or 0) and 1", True),
        ("1 and 0 or 1", True),
        ("not not 1", True),
        ("0 or 0 and 1", False),
    ]
    for expr, expected in test_cases:
        result = evaluator.check_precedence(expr)
        assert result == expected, f"Failed for {expr}: expected {expected}, got {result}"
    print("All tests passed.")