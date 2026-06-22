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
            elif char == '!':
                tokens.append(('NOT', 'not'))
                i += 1
            elif char == '&' and i + 1 < length and expression_string[i + 1] == '&':
                tokens.append(('AND', 'and'))
                i += 2
            elif char == '|' and i + 1 < length and expression_string[i + 1] == '|':
                tokens.append(('OR', 'or'))
                i += 2
            elif char.isalpha():
                start = i
                while i < length and (expression_string[i].isalnum() or expression_string[i] == '_'):
                    i += 1
                word = expression_string[start:i].lower()
                if word in ('true', 'false'):
                    tokens.append(('BOOL', word == 'true'))
                else:
                    raise ValueError(f"Unknown variable: {expression_string[start:i]}")
            else:
                raise ValueError(f"Unexpected character: {char}")
        return tokens

    def _parse_expression(self, tokens, index):
        left, index = self._parse_or(tokens, index)
        return left, index

    def _parse_or(self, tokens, index):
        left, index = self._parse_and(tokens, index)
        while index < len(tokens) and tokens[index][0] == 'OR':
            op = tokens[index][1]
            index += 1
            right, index = self._parse_and(tokens, index)
            left = left or right
        return left, index

    def _parse_and(self, tokens, index):
        left, index = self._parse_not(tokens, index)
        while index < len(tokens) and tokens[index][0] == 'AND':
            op = tokens[index][1]
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
        if index >= len(tokens):
            raise ValueError("Unexpected end of expression")
        token_type, token_value = tokens[index]
        if token_type == 'LPAREN':
            index += 1
            val, index = self._parse_expression(tokens, index)
            if index >= len(tokens) or tokens[index][0] != 'RPAREN':
                raise ValueError("Missing closing parenthesis")
            index += 1
            return val, index
        elif token_type == 'BOOL':
            return token_value, index + 1
        else:
            raise ValueError(f"Unexpected token: {token_type}")

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    test_cases = [
        "true and false",
        "true or false",
        "not true",
        "(true or false) and false",
        "true and (false or true)",
        "not (true and false)",
    ]
    for expr in test_cases:
        result = evaluator.check_precedence(expr)
        print(f"{expr} = {result}")