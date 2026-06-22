class BooleanExpressionParser:
    def __init__(self, expression: str):
        self.expression = expression
        self.pos = 0
        self.tokens = self._tokenize(expression)

    def _tokenize(self, expr: str) -> list:
        tokens = []
        i = 0
        length = len(expr)
        while i < length:
            char = expr[i]
            if char.isspace():
                i += 1
                continue
            if char in ('(', ')'):
                tokens.append(char)
                i += 1
                continue
            if char in ('T', 't') and expr[i:i+4].lower() == 'true':
                tokens.append('True')
                i += 4
                continue
            if char in ('F', 'f') and expr[i:i+5].lower() == 'false':
                tokens.append('False')
                i += 5
                continue
            if char in ('A', 'a') and expr[i:i+3].lower() == 'and':
                tokens.append('AND')
                i += 3
                continue
            if char in ('O', 'o') and expr[i:i+2].lower() == 'or':
                tokens.append('OR')
                i += 2
                continue
            if char in ('N', 'n') and expr[i:i+3].lower() == 'not':
                tokens.append('NOT')
                i += 3
                continue
            raise ValueError(f"Unexpected character at index {i}: {char}")
        return tokens

    def parse(self) -> bool:
        if not self.tokens:
            return False
        result, _ = self._parse_or(0)
        if self.pos < len(self.tokens):
            raise ValueError("Unexpected token after expression")
        return result

    def _parse_or(self, pos: int):
        left, next_pos = self._parse_and(pos)
        while next_pos < len(self.tokens) and self.tokens[next_pos] == 'OR':
            next_pos += 1
            right, next_pos = self._parse_and(next_pos)
            left = left or right
        return left, next_pos

    def _parse_and(self, pos: int):
        left, next_pos = self._parse_not(pos)
        while next_pos < len(self.tokens) and self.tokens[next_pos] == 'AND':
            next_pos += 1
            right, next_pos = self._parse_not(next_pos)
            left = left and right
        return left, next_pos

    def _parse_not(self, pos: int):
        if pos < len(self.tokens) and self.tokens[pos] == 'NOT':
            operand, next_pos = self._parse_not(pos + 1)
            return not operand, next_pos
        return self._parse_primary(pos)

    def _parse_primary(self, pos: int):
        if pos >= len(self.tokens):
            raise ValueError("Unexpected end of expression")
        token = self.tokens[pos]
        if token == '(':
            operand, next_pos = self._parse_or(pos + 1)
            if next_pos >= len(self.tokens) or self.tokens[next_pos] != ')':
                raise ValueError("Missing closing parenthesis")
            return operand, next_pos + 1
        if token == 'True':
            return True, pos + 1
        if token == 'False':
            return False, pos + 1
        raise ValueError(f"Unexpected token: {token}")

def evaluate_expression(expression: str) -> bool:
    parser = BooleanExpressionParser(expression)
    return parser.parse()

if __name__ == '__main__':
    expr1 = "True AND False OR True"
    result1 = evaluate_expression(expr1)
    print(result1)

    expr2 = "NOT (True AND False) OR False"
    result2 = evaluate_expression(expr2)
    print(result2)