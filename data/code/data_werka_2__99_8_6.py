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
            elif char == '&' and i + 1 < length and expression_string[i + 1] == '&':
                tokens.append(('AND', '&&'))
                i += 2
            elif char == '|' and i + 1 < length and expression_string[i + 1] == '|':
                tokens.append(('OR', '||'))
                i += 2
            elif char == '!':
                tokens.append(('NOT', '!'))
                i += 1
            elif char == 't' and i + 3 < length and expression_string[i:i+4].lower() == 'true':
                tokens.append(('BOOL', True))
                i += 4
            elif char == 'f' and i + 3 < length and expression_string[i:i+4].lower() == 'false':
                tokens.append(('BOOL', False))
                i += 4
            else:
                raise ValueError(f"Unexpected character: {char}")
        return tokens

    def _parse_or(self, tokens, index):
        left, index = self._parse_and(tokens, index)
        while index < len(tokens) and tokens[index][0] == 'OR':
            index += 1
            right, index = self._parse_and(tokens, index)
            left = left or right
        return left, index

    def _parse_and(self, tokens, index):
        left, index = self._parse_not(tokens, index)
        while index < len(tokens) and tokens[index][0] == 'AND':
            index += 1
            right, index = self._parse_not(tokens, index)
            left = left and right
        return left, index

    def _parse_not(self, tokens, index):
        if index < len(tokens) and tokens[index][0] == 'NOT':
            index += 1
            val, index = self._parse_not(tokens, index)
            return not val, index
        return self._parse_primary(tokens, index)

    def _parse_primary(self, tokens, index):
        if index < len(tokens) and tokens[index][0] == 'LPAREN':
            index += 1
            val, index = self._parse_or(tokens, index)
            if index < len(tokens) and tokens[index][0] == 'RPAREN':
                index += 1
            return val, index
        if index < len(tokens) and tokens[index][0] == 'BOOL':
            return tokens[index][1], index + 1
        raise ValueError("Unexpected token")

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    expr1 = "true && false || true"
    result1 = evaluator.check_precedence(expr1)
    print(result1)
    expr2 = "true || false && false"
    result2 = evaluator.check_precedence(expr2)
    print(result2)
    expr3 = "!(true && false)"
    result3 = evaluator.check_precedence(expr3)
    print(result3)
    expr4 = "true && (false || true)"
    result4 = evaluator.check_precedence(expr4)
    print(result4)