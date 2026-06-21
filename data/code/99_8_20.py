class BooleanEvaluator:
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
            elif char == '!' and i + 1 < length and expression_string[i + 1].isdigit():
                tokens.append(('NOT', 'not'))
                i += 1
            elif char.isdigit():
                num = char
                i += 1
                while i < length and expression_string[i].isdigit():
                    num += expression_string[i]
                    i += 1
                tokens.append(('NUMBER', int(num)))
            elif i + 1 < length and expression_string[i:i+2] == 'or':
                tokens.append(('OR', 'or'))
                i += 2
            elif i + 2 < length and expression_string[i:i+3] == 'and':
                tokens.append(('AND', 'and'))
                i += 3
            elif i + 2 < length and expression_string[i:i+3] == 'not':
                tokens.append(('NOT', 'not'))
                i += 3
            else:
                raise ValueError(f"Unknown character: {char}")
        return tokens

    def _parse_expression(self, tokens, index):
        result, index = self._parse_or(tokens, index)
        return result, index

    def _parse_or(self, tokens, index):
        left, index = self._parse_and(tokens, index)
        while index < len(tokens) and tokens[index][0] == 'OR':
            op = tokens[index][1]
            index += 1
            right, index = self._parse_and(tokens, index)
            left = (op, left, right)
        return left, index

    def _parse_and(self, tokens, index):
        left, index = self._parse_not(tokens, index)
        while index < len(tokens) and tokens[index][0] == 'AND':
            op = tokens[index][1]
            index += 1
            right, index = self._parse_not(tokens, index)
            left = (op, left, right)
        return left, index

    def _parse_not(self, tokens, index):
        if index < len(tokens) and tokens[index][0] == 'NOT':
            op = tokens[index][1]
            index += 1
            right, index = self._parse_primary(tokens, index)
            return (op, right)
        return self._parse_primary(tokens, index)

    def _parse_primary(self, tokens, index):
        token = tokens[index]
        if token[0] == 'NUMBER':
            return token[1], index + 1
        elif token[0] == 'LPAREN':
            index += 1
            result, index = self._parse_expression(tokens, index)
            if index < len(tokens) and tokens[index][0] == 'RPAREN':
                index += 1
                return result, index
            else:
                raise ValueError("Mismatched parentheses")
        else:
            raise ValueError(f"Unexpected token: {token}")

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    print(evaluator.check_precedence("1 and 0 or 1"))
    print(evaluator.check_precedence("(1 or 0) and 1"))
    print(evaluator.check_precedence("not 1 and 0"))
    print(evaluator.check_precedence("1"))