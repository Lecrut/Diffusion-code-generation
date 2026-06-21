class BooleanExpressionEvaluator:
    def __init__(self, expression: str, variables: dict):
        self.expression = expression
        self.variables = variables
        self.tokens = []
        self.pos = 0

    def evaluate(self) -> bool:
        self.tokens = self._tokenize(self.expression)
        self.pos = 0
        if not self.tokens:
            return False
        result, _ = self._parse_or(self.tokens, 0)
        return result

    def _tokenize(self, expr: str) -> list:
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
            elif char in ('and', 'or', 'not'):
                tokens.append(('OP', char))
                i += 1
            elif char.isalpha() or char == '_':
                start = i
                while i < length and (expr[i].isalnum() or expr[i] == '_'):
                    i += 1
                tokens.append(('VAR', expr[start:i]))
            elif char == '(':
                tokens.append(('LPAREN', '('))
                i += 1
            else:
                raise ValueError(f"Unexpected character: {char}")
        return tokens

    def _parse_or(self, tokens: list, pos: int) -> tuple:
        left, pos = self._parse_and(tokens, pos)
        while pos < len(tokens) and tokens[pos][0] == 'OP' and tokens[pos][1] == 'or':
            pos += 1
            right, pos = self._parse_and(tokens, pos)
            left = left or right
        return left, pos

    def _parse_and(self, tokens: list, pos: int) -> tuple:
        left, pos = self._parse_not(tokens, pos)
        while pos < len(tokens) and tokens[pos][0] == 'OP' and tokens[pos][1] == 'and':
            pos += 1
            right, pos = self._parse_not(tokens, pos)
            left = left and right
        return left, pos

    def _parse_not(self, tokens: list, pos: int) -> tuple:
        if pos < len(tokens) and tokens[pos][0] == 'OP' and tokens[pos][1] == 'not':
            pos += 1
            val, pos = self._parse_not(tokens, pos)
            return not val, pos
        return self._parse_primary(tokens, pos)

    def _parse_primary(self, tokens: list, pos: int) -> tuple:
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
        elif token_type == 'VAR':
            if token_val not in self.variables:
                raise ValueError(f"Variable {token_val} not defined")
            val = self.variables[token_val]
            if not isinstance(val, bool):
                raise ValueError(f"Variable {token_val} must be a boolean, got {type(val).__name__}")
            return val, pos + 1
        else:
            raise ValueError(f"Unexpected token: {token_val}")

if __name__ == "__main__":
    evaluator1 = BooleanExpressionEvaluator("True and False", {"True": True, "False": False})
    print(evaluator1.evaluate())

    evaluator2 = BooleanExpressionEvaluator("(True or False) and True", {"True": True, "False": False})
    print(evaluator2.evaluate())

    evaluator3 = BooleanExpressionEvaluator("not False", {"False": False})
    print(evaluator3.evaluate())

    evaluator4 = BooleanExpressionEvaluator("True or False and False", {"True": True, "False": False})
    print(evaluator4.evaluate())