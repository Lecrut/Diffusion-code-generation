class BooleanEvaluator:
    def check_precedence(self, expression_string):
        tokens = self._tokenize(expression_string)
        if not tokens:
            return False
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
            elif char == '&' and i + 1 < length and expr[i + 1] == '&':
                tokens.append(('AND', '&&'))
                i += 2
            elif char == '|' and i + 1 < length and expr[i + 1] == '|':
                tokens.append(('OR', '||'))
                i += 2
            elif char == '!' and (i == 0 or expr[i - 1] in ('(', ' ', '&', '|', '!', '&&', '||')):
                tokens.append(('NOT', '!'))
                i += 1
            elif char == 'n' and i + 3 < length and expr[i:i+4] == 'not ':
                tokens.append(('NOT', 'not'))
                i += 4
            elif char == 't' and i + 3 < length and expr[i:i+4] == 'true':
                tokens.append(('BOOL', True))
                i += 4
            elif char == 'f' and i + 4 < length and expr[i:i+5] == 'false':
                tokens.append(('BOOL', False))
                i += 5
            elif char == '1':
                tokens.append(('BOOL', True))
                i += 1
            elif char == '0':
                tokens.append(('BOOL', False))
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
            return not val
        return self._parse_primary(tokens, pos)

    def _parse_primary(self, tokens, pos):
        if pos >= len(tokens):
            raise ValueError("Unexpected end of expression")
        token_type, token_val = tokens[pos]
        if token_type == 'BOOL':
            return token_val, pos + 1
        if token_type == 'LPAREN':
            val, pos = self._parse_or(tokens, pos + 1)
            if pos >= len(tokens) or tokens[pos][0] != 'RPAREN':
                raise ValueError("Missing closing parenthesis")
            return val, pos + 1
        raise ValueError(f"Unexpected token: {token_val}")

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    expr1 = "true && false || true"
    result1 = evaluator.check_precedence(expr1)
    print(result1)
    
    expr2 = "!(true && false) || false"
    result2 = evaluator.check_precedence(expr2)
    print(result2)
    
    expr3 = "true || false && false"
    result3 = evaluator.check_precedence(expr3)
    print(result3)
    
    expr4 = "(true || false) && false"
    result4 = evaluator.check_precedence(expr4)
    print(result4)
    
    expr5 = "!!true"
    result5 = evaluator.check_precedence(expr5)
    print(result5)