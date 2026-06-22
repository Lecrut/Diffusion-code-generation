class BooleanExpressionEvaluator:
    def __init__(self, expression: str, variables: dict):
        self.expression = expression
        self.variables = variables
        self.tokens = []
        self.pos = 0

    def tokenize(self):
        expr = self.expression.replace('(', ' ( ').replace(')', ' ) ')
        expr = expr.replace('and', ' and ').replace('or', ' or ').replace('not', ' not ')
        parts = expr.split()
        valid_tokens = []
        for part in parts:
            if part:
                valid_tokens.append(part)
        self.tokens = valid_tokens
        return self.tokens

    def evaluate(self):
        self.tokenize()
        self.pos = 0
        if not self.tokens:
            return False
        result, self.pos = self.parse_or(self.pos)
        return result

    def parse_or(self, pos):
        left, pos = self.parse_and(pos)
        while pos < len(self.tokens) and self.tokens[pos] == 'or':
            pos += 1
            right, pos = self.parse_and(pos)
            left = left or right
        return left, pos

    def parse_and(self, pos):
        left, pos = self.parse_not(pos)
        while pos < len(self.tokens) and self.tokens[pos] == 'and':
            pos += 1
            right, pos = self.parse_not(pos)
            left = left and right
        return left, pos

    def parse_not(self, pos):
        if pos < len(self.tokens) and self.tokens[pos] == 'not':
            pos += 1
            val, pos = self.parse_not(pos)
            return not val, pos
        return self.parse_primary(pos)

    def parse_primary(self, pos):
        if pos >= len(self.tokens):
            raise ValueError("Unexpected end of expression")
        
        token = self.tokens[pos]
        
        if token == '(':
            pos += 1
            result, pos = self.parse_or(pos)
            if pos >= len(self.tokens) or self.tokens[pos] != ')':
                raise ValueError("Missing closing parenthesis")
            pos += 1
            return result, pos
        
        if token == 'and' or token == 'or':
            raise ValueError(f"Unexpected operator: {token}")
        
        if token in ('true', 'True', '1'):
            return True, pos + 1
        
        if token in ('false', 'False', '0'):
            return False, pos + 1
        
        if token not in self.variables:
            raise ValueError(f"Undefined variable: {token}")
        
        val = self.variables[token]
        if not isinstance(val, bool):
            raise ValueError(f"Variable {token} must be boolean")
        
        return val, pos + 1

if __name__ == '__main__':
    evaluator = BooleanExpressionEvaluator('((A and B) or C)', {'A': True, 'B': False, 'C': True})
    print(evaluator.evaluate())