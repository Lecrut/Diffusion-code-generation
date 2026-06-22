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
                tokens.append(('NOT', '!'))
                i += 1
            elif i + 1 < length and expression_string[i:i+2] == '&&':
                tokens.append(('AND', '&&'))
                i += 2
            elif i + 1 < length and expression_string[i:i+2] == '||':
                tokens.append(('OR', '||'))
                i += 2
            elif char in ('&', '|'):
                if char == '&':
                    tokens.append(('AND', '&'))
                else:
                    tokens.append(('OR', '|'))
                i += 1
            elif char in ('T', 't', 'F', 'f', '1', '0'):
                if char in ('T', 't', '1'):
                    tokens.append(('BOOL', True))
                else:
                    tokens.append(('BOOL', False))
                i += 1
            else:
                raise ValueError(f"Unexpected character: {char}")
        return tokens

    def _parse_or(self, tokens, index):
        left, index = self._parse_and(tokens, index)
        while index < len(tokens) and tokens[index][0] == 'OR':
            operator = tokens[index][1]
            index += 1
            right, index = self._parse_and(tokens, index)
            left = left or right
        return left, index

    def _parse_and(self, tokens, index):
        left, index = self._parse_not(tokens, index)
        while index < len(tokens) and tokens[index][0] == 'AND':
            operator = tokens[index][1]
            index += 1
            right, index = self._parse_not(tokens, index)
            left = left and right
        return left, index

    def _parse_not(self, tokens, index):
        if index < len(tokens) and tokens[index][0] == 'NOT':
            index += 1
            value, index = self._parse_not(tokens, index)
            return not value, index
        return self._parse_primary(tokens, index)

    def _parse_primary(self, tokens, index):
        if index >= len(tokens):
            raise ValueError("Unexpected end of expression")
        token_type, token_value = tokens[index]
        if token_type == 'LPAREN':
            index += 1
            value, index = self._parse_or(tokens, index)
            if index >= len(tokens) or tokens[index][0] != 'RPAREN':
                raise ValueError("Missing closing parenthesis")
            index += 1
            return value, index
        elif token_type == 'BOOL':
            return token_value, index + 1
        else:
            raise ValueError(f"Unexpected token: {token_value}")

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    expr1 = "True && False || True"
    result1 = evaluator.check_precedence(expr1)
    print(result1)
    expr2 = "!(True && False) || False"
    result2 = evaluator.check_precedence(expr2)
    print(result2)
    expr3 = "True || False && False"
    result3 = evaluator.check_precedence(expr3)
    print(result3)
    expr4 = "!(True || False) && True"
    result4 = evaluator.check_precedence(expr4)
    print(result4)
    expr5 = "True && (False || True)"
    result5 = evaluator.check_precedence(expr5)
    print(result5)