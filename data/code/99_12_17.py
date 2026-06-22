class FlagEvaluator:
    def __init__(self, flags: dict):
        self.flags = flags

    def evaluate(self, expression: str) -> bool:
        if not isinstance(expression, str):
            raise ValueError("Expression must be a string")
        
        cleaned = expression.replace(" ", "")
        if not cleaned:
            raise ValueError("Expression cannot be empty")
        
        tokens = self._tokenize(cleaned)
        if not tokens:
            raise ValueError("No valid tokens found")
        
        result = self._parse_or(tokens)
        return result

    def _tokenize(self, expr: str) -> list:
        tokens = []
        i = 0
        while i < len(expr):
            char = expr[i]
            if char == '(':
                tokens.append(('LPAREN', '('))
                i += 1
            elif char == ')':
                tokens.append(('RPAREN', ')'))
                i += 1
            elif char == '&':
                if i + 1 < len(expr) and expr[i+1] == '&':
                    tokens.append(('AND', '&&'))
                    i += 2
                else:
                    raise ValueError(f"Invalid character at position {i}")
            elif char == '|':
                if i + 1 < len(expr) and expr[i+1] == '|':
                    tokens.append(('OR', '||'))
                    i += 2
                else:
                    raise ValueError(f"Invalid character at position {i}")
            elif char == '!':
                tokens.append(('NOT', '!'))
                i += 1
            elif char.isalpha() or char == '_':
                start = i
                while i < len(expr) and (expr[i].isalnum() or expr[i] == '_'):
                    i += 1
                tokens.append(('FLAG', expr[start:i]))
            else:
                raise ValueError(f"Invalid character at position {i}")
        return tokens

    def _parse_or(self, tokens: list) -> bool:
        left = self._parse_and(tokens)
        
        while tokens and tokens[0][0] == 'OR':
            tokens.pop(0)
            right = self._parse_and(tokens)
            if left:
                return True
            left = right
        return left

    def _parse_and(self, tokens: list) -> bool:
        left = self._parse_not(tokens)
        
        while tokens and tokens[0][0] == 'AND':
            tokens.pop(0)
            right = self._parse_not(tokens)
            if not left:
                return False
            left = right
        return left

    def _parse_not(self, tokens: list) -> bool:
        if tokens and tokens[0][0] == 'NOT':
            tokens.pop(0)
            operand = self._parse_not(tokens)
            return not operand
        
        return self._parse_primary(tokens)

    def _parse_primary(self, tokens: list) -> bool:
        if not tokens:
            raise ValueError("Unexpected end of expression")
        
        token_type, token_value = tokens[0]
        
        if token_type == 'LPAREN':
            tokens.pop(0)
            result = self._parse_or(tokens)
            if not tokens or tokens[0][0] != 'RPAREN':
                raise ValueError("Missing closing parenthesis")
            tokens.pop(0)
            return result
        
        if token_type == 'FLAG':
            tokens.pop(0)
            flag_name = token_value
            if flag_name not in self.flags:
                raise ValueError(f"Unknown flag: {flag_name}")
            return bool(self.flags[flag_name])
        
        raise ValueError(f"Unexpected token: {token_type}")

if __name__ == '__main__':
    flags = {
        'A': True,
        'B': False,
        'C': True,
        'D': False
    }
    
    evaluator = FlagEvaluator(flags)
    
    result1 = evaluator.evaluate("A && B")
    print(result1)
    
    result2 = evaluator.evaluate("A || B")
    print(result2)
    
    result3 = evaluator.evaluate("(A || B) && C")
    print(result3)
    
    result4 = evaluator.evaluate("!B && C")
    print(result4)
    
    result5 = evaluator.evaluate("A && (B || D)")
    print(result5)