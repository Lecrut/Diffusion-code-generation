class FlagEvaluator:
    def __init__(self, flags):
        if not isinstance(flags, dict):
            raise ValueError("Flags must be a dictionary")
        self.flags = flags

    def evaluate(self, expression):
        if not isinstance(expression, str):
            raise ValueError("Expression must be a string")
        
        tokens = self._tokenize(expression)
        if not tokens:
            return False
        
        result = self._parse_or(tokens)
        return result

    def _tokenize(self, expression):
        tokens = []
        i = 0
        while i < len(expression):
            char = expression[i]
            if char.isspace():
                i += 1
                continue
            if char == '(':
                tokens.append('(')
                i += 1
            elif char == ')':
                tokens.append(')')
                i += 1
            elif char == '&' and i + 1 < len(expression) and expression[i + 1] == '&':
                tokens.append('AND')
                i += 2
            elif char == '|' and i + 1 < len(expression) and expression[i + 1] == '|':
                tokens.append('OR')
                i += 2
            elif char == '!':
                tokens.append('NOT')
                i += 1
            elif char.isalpha() or char == '_':
                start = i
                while i < len(expression) and (expression[i].isalnum() or expression[i] == '_'):
                    i += 1
                tokens.append(expression[start:i])
            else:
                raise ValueError(f"Unexpected character: {char}")
        return tokens

    def _parse_or(self, tokens):
        left = self._parse_and(tokens)
        while tokens and tokens[0] == 'OR':
            tokens.pop(0)
            right = self._parse_and(tokens)
            if left:
                return True
            left = right
        return left

    def _parse_and(self, tokens):
        left = self._parse_not(tokens)
        while tokens and tokens[0] == 'AND':
            tokens.pop(0)
            right = self._parse_not(tokens)
            if not left:
                return False
            left = right
        return left

    def _parse_not(self, tokens):
        if tokens and tokens[0] == 'NOT':
            tokens.pop(0)
            value = self._parse_not(tokens)
            return not value
        return self._parse_primary(tokens)

    def _parse_primary(self, tokens):
        if not tokens:
            raise ValueError("Unexpected end of expression")
        
        token = tokens.pop(0)
        
        if token == '(':
            value = self._parse_or(tokens)
            if not tokens or tokens[0] != ')':
                raise ValueError("Missing closing parenthesis")
            tokens.pop(0)
            return value
        
        if token == 'AND' or token == 'OR':
            raise ValueError(f"Unexpected operator: {token}")
        
        if token in self.flags:
            return bool(self.flags[token])
        
        raise ValueError(f"Unknown flag: {token}")

if __name__ == '__main__':
    evaluator = FlagEvaluator({
        'A': True,
        'B': False,
        'C': True,
        'D': False
    })
    
    result1 = evaluator.evaluate('A & B | C')
    print(result1)
    
    result2 = evaluator.evaluate('(A | B) & (C | D)')
    print(result2)
    
    result3 = evaluator.evaluate('!A & B')
    print(result3)
    
    result4 = evaluator.evaluate('A & (B | C) & D')
    print(result4)