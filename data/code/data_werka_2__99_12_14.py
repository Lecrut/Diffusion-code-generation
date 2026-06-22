class FlagEvaluator:
    def __init__(self, flags):
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
        current = ""
        i = 0
        while i < len(expression):
            char = expression[i]
            if char == ' ':
                if current:
                    tokens.append(current)
                    current = ""
            elif char in ('&', '|', '!', '(', ')'):
                if current:
                    tokens.append(current)
                    current = ""
                tokens.append(char)
            else:
                current += char
            i += 1
        if current:
            tokens.append(current)
        return tokens

    def _parse_or(self, tokens):
        left = self._parse_and(tokens)
        while tokens and tokens[0] == '|':
            tokens.pop(0)
            right = self._parse_and(tokens)
            left = left or right
        return left

    def _parse_and(self, tokens):
        left = self._parse_not(tokens)
        while tokens and tokens[0] == '&':
            tokens.pop(0)
            right = self._parse_not(tokens)
            left = left and right
        return left

    def _parse_not(self, tokens):
        if tokens and tokens[0] == '!':
            tokens.pop(0)
            val = self._parse_not(tokens)
            return not val
        return self._parse_primary(tokens)

    def _parse_primary(self, tokens):
        if not tokens:
            raise ValueError("Unexpected end of expression")
        
        token = tokens.pop(0)
        
        if token == '(':
            result = self._parse_or(tokens)
            if not tokens or tokens[0] != ')':
                raise ValueError("Missing closing parenthesis")
            tokens.pop(0)
            return result
        
        if token == ')':
            raise ValueError("Unexpected closing parenthesis")
        
        if token in ('&', '|', '!'):
            raise ValueError(f"Unexpected operator: {token}")
        
        if token.lower() == 'true':
            return True
        if token.lower() == 'false':
            return False
        
        if token in self.flags:
            return self.flags[token]
        
        raise ValueError(f"Unknown flag: {token}")

if __name__ == '__main__':
    flags = {
        'A': True,
        'B': False,
        'C': True,
        'D': False
    }
    
    evaluator = FlagEvaluator(flags)
    
    result1 = evaluator.evaluate("A & B | C")
    print(result1)
    
    result2 = evaluator.evaluate("!A | (B & C)")
    print(result2)
    
    result3 = evaluator.evaluate("A & (B | C) & D")
    print(result3)