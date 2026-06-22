class BooleanEvaluator:
    def __init__(self):
        self.operators = ('or', 'and', 'not')
        self.prec = {'or': 1, 'and': 2, 'not': 3}

    def check_precedence(self, expression_string):
        tokens = self._tokenize(expression_string)
        if not tokens:
            raise ValueError("Empty expression")
        result, _ = self._parse_or(tokens, 0)
        if _ < len(tokens):
            raise ValueError("Unexpected tokens remaining")
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
            elif char.isalpha():
                start = i
                while i < length and (expression_string[i].isalnum() or expression_string[i] == '_'):
                    i += 1
                word = expression_string[start:i]
                if word in self.operators:
                    tokens.append(('OP', word))
                elif word in ('True', 'False'):
                    tokens.append(('BOOL', word == 'True'))
                else:
                    raise ValueError(f"Unknown identifier: {word}")
            else:
                raise ValueError(f"Unknown character: {char}")
        return tokens

    def _parse_or(self, tokens, pos):
        left, pos = self._parse_and(tokens, pos)
        while pos < len(tokens) and tokens[pos][0] == 'OP' and tokens[pos][1] == 'or':
            pos += 1
            right, pos = self._parse_and(tokens, pos)
            left = left or right
        return left, pos

    def _parse_and(self, tokens, pos):
        left, pos = self._parse_not(tokens, pos)
        while pos < len(tokens) and tokens[pos][0] == 'OP' and tokens[pos][1] == 'and':
            pos += 1
            right, pos = self._parse_not(tokens, pos)
            left = left and right
        return left, pos

    def _parse_not(self, tokens, pos):
        if pos < len(tokens) and tokens[pos][0] == 'OP' and tokens[pos][1] == 'not':
            pos += 1
            operand, pos = self._parse_not(tokens, pos)
            return not operand
        return self._parse_primary(tokens, pos)

    def _parse_primary(self, tokens, pos):
        if pos >= len(tokens):
            raise ValueError("Unexpected end of expression")
        token_type, token_val = tokens[pos]
        if token_type == 'LPAREN':
            pos += 1
            val, pos = self._parse_or(tokens, pos)
            if pos >= len(tokens) or tokens[pos][0] != 'RPAREN':
                raise ValueError("Missing closing parenthesis")
            pos += 1
            return val, pos
        elif token_type == 'BOOL':
            return token_val, pos + 1
        else:
            raise ValueError(f"Unexpected token: {token_val}")

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    print(evaluator.check_precedence("True and False"))
    print(evaluator.check_precedence("True or False"))
    print(evaluator.check_precedence("not True"))
    print(evaluator.check_precedence("(True or False) and False"))