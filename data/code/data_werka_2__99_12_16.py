from functools import reduce

class FlagExpression:
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
            if char == '(':
                if current:
                    tokens.append(current)
                    current = ""
                tokens.append('(')
            elif char == ')':
                if current:
                    tokens.append(current)
                    current = ""
                tokens.append(')')
            elif char in ('&', '|'):
                if current:
                    tokens.append(current)
                    current = ""
                tokens.append(char)
            elif char == ' ':
                if current:
                    tokens.append(current)
                    current = ""
            else:
                current += char
            i += 1
        if current:
            tokens.append(current)
        return tokens

    def _parse_or(self, tokens):
        results = []
        current = self._parse_and(tokens)
        results.append(current)
        
        while tokens and tokens[0] == '|':
            tokens.pop(0)
            next_val = self._parse_and(tokens)
            results.append(next_val)
        
        return reduce(lambda a, b: a or b, results)

    def _parse_and(self, tokens):
        results = []
        current = self._parse_not(tokens)
        results.append(current)
        
        while tokens and tokens[0] == '&':
            tokens.pop(0)
            next_val = self._parse_not(tokens)
            results.append(next_val)
        
        return reduce(lambda a, b: a and b, results)

    def _parse_not(self, tokens):
        if tokens and tokens[0] == '!':
            tokens.pop(0)
            val = self._parse_primary(tokens)
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
        
        if token in ('&', '|'):
            raise ValueError(f"Unexpected operator: {token}")
        
        return self._resolve_flag(token)

    def _resolve_flag(self, flag_name):
        if flag_name in self.flags:
            return bool(self.flags[flag_name])
        raise ValueError(f"Unknown flag: {flag_name}")

if __name__ == '__main__':
    flags = {
        'A': True,
        'B': False,
        'C': True,
        'D': False
    }
    
    expr = FlagExpression(flags)
    
    result1 = expr.evaluate("A & B | C")
    print(result1)
    
    result2 = expr.evaluate("(A | B) & (C | D)")
    print(result2)
    
    result3 = expr.evaluate("!B & C")
    print(result3)
    
    result4 = expr.evaluate("A & (B | C) & D")
    print(result4)