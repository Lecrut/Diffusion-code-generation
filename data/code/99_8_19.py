class BooleanEvaluator:
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
            elif char == '!':
                tokens.append(('NOT', 'not'))
                i += 1
            elif char == '&' and i + 1 < length and expression_string[i + 1] == '&':
                tokens.append(('AND', 'and'))
                i += 2
            elif char == '|' and i + 1 < length and expression_string[i + 1] == '|':
                tokens.append(('OR', 'or'))
                i += 2
            elif char in 'aA' and i + 3 < length and expression_string[i + 1:i + 4].lower() == 'nd':
                tokens.append(('AND', 'and'))
                i += 4
            elif char in 'oO' and i + 2 < length and expression_string[i + 1:i + 3].lower() == 'r':
                tokens.append(('OR', 'or'))
                i += 3
            elif char in 'tT' and i + 4 < length and expression_string[i + 1:i + 5].lower() == 'rue':
                tokens.append(('BOOL', True))
                i += 5
            elif char in 'fF' and i + 5 < length and expression_string[i + 1:i + 6].lower() == 'alse':
                tokens.append(('BOOL', False))
                i += 6
            elif char == 'n' and i + 3 < length and expression_string[i + 1:i + 4].lower() == 'ot':
                tokens.append(('NOT', 'not'))
                i += 4
            else:
                raise ValueError(f"Unexpected character: {char}")
        return tokens

    def _parse_or(self, tokens, pos):
        left, pos = self._parse_and(tokens, pos)
        while pos < len(tokens) and tokens[pos][0] == 'OR':
            pos += 1
            right, pos = self._parse_and(tokens, pos)
            left = ('or', left, right)
        return left, pos

    def _parse_and(self, tokens, pos):
        left, pos = self._parse_not(tokens, pos)
        while pos < len(tokens) and tokens[pos][0] == 'AND':
            pos += 1
            right, pos = self._parse_not(tokens, pos)
            left = ('and', left, right)
        return left, pos

    def _parse_not(self, tokens, pos):
        if pos < len(tokens) and tokens[pos][0] == 'NOT':
            pos += 1
            operand, pos = self._parse_not(tokens, pos)
            return ('not', operand), pos
        return self._parse_primary(tokens, pos)

    def _parse_primary(self, tokens, pos):
        if pos < len(tokens) and tokens[pos][0] == 'LPAREN':
            pos += 1
            expr, pos = self._parse_or(tokens, pos)
            if pos < len(tokens) and tokens[pos][0] == 'RPAREN':
                pos += 1
            return expr, pos
        if pos < len(tokens) and tokens[pos][0] == 'BOOL':
            return tokens[pos][1], pos + 1
        raise ValueError("Expected boolean literal or parenthesis")

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    print(evaluator.check_precedence("True and False or True"))
    print(evaluator.check_precedence("(True or False) and True"))
    print(evaluator.check_precedence("not False"))