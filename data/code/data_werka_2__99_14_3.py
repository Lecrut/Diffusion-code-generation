class BooleanExpressionEvaluator:
    def __init__(self, expression: str):
        self.expression = expression
        self.tokens = []
        self.pos = 0
        self._tokenize()

    def _tokenize(self):
        raw = self.expression.replace('AND', 'and').replace('OR', 'or').replace('NOT', 'not')
        raw = raw.replace('True', 'True').replace('False', 'False')
        words = raw.split()
        for word in words:
            if word in ('(', ')'):
                self.tokens.append(word)
            elif word in ('and', 'or', 'not'):
                self.tokens.append(word)
            elif word in ('True', 'False'):
                self.tokens.append(word)
            else:
                raise ValueError(f"Unknown token: {word}")

    def evaluate(self) -> bool:
        if not self.tokens:
            raise ValueError("Empty expression")
        result, end_pos = self._parse_or(0)
        if end_pos != len(self.tokens):
            raise ValueError("Unexpected tokens at end of expression")
        return result

    def _parse_or(self, index: int) -> tuple:
        left, index = self._parse_and(index)
        while index < len(self.tokens) and self.tokens[index] == 'or':
            self._consume('or', index)
            index += 1
            right, index = self._parse_and(index)
            left = left or right
        return left, index

    def _parse_and(self, index: int) -> tuple:
        left, index = self._parse_not(index)
        while index < len(self.tokens) and self.tokens[index] == 'and':
            self._consume('and', index)
            index += 1
            right, index = self._parse_not(index)
            left = left and right
        return left, index

    def _parse_not(self, index: int) -> tuple:
        if index < len(self.tokens) and self.tokens[index] == 'not':
            self._consume('not', index)
            index += 1
            value, index = self._parse_not(index)
            return not value, index
        return self._parse_primary(index)

    def _parse_primary(self, index: int) -> tuple:
        if index >= len(self.tokens):
            raise ValueError("Unexpected end of expression")
        
        token = self.tokens[index]
        
        if token == '(':
            self._consume('(', index)
            index += 1
            value, index = self._parse_or(index)
            self._consume(')', index)
            return value, index + 1
        
        if token in ('True', 'False'):
            return token == 'True', index + 1
        
        raise ValueError(f"Unexpected token: {token}")

    def _consume(self, expected: str, index: int):
        if index >= len(self.tokens) or self.tokens[index] != expected:
            actual = self.tokens[index] if index < len(self.tokens) else "END"
            raise ValueError(f"Expected '{expected}', got '{actual}'")

def evaluate_boolean_expression(expression: str) -> bool:
    evaluator = BooleanExpressionEvaluator(expression)
    return evaluator.evaluate()

if __name__ == '__main__':
    expressions = [
        "True and False",
        "True or False",
        "not True",
        "(True or False) and False",
        "True and (False or True)",
        "not (True and False)",
        "True or not False",
    ]

    for expr in expressions:
        result = evaluate_boolean_expression(expr)
        print(result)