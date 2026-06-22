class FlagEvaluator:
    def __init__(self, flags: dict):
        self.flags = flags

    def evaluate(self, expression: str) -> bool:
        if not expression:
            return False
        
        tokens = self._tokenize(expression)
        if not tokens:
            return False
        
        result = self._parse_or(tokens)
        return result

    def _tokenize(self, expression: str) -> list:
        tokens = []
        i = 0
        length = len(expression)
        
        while i < length:
            char = expression[i]
            
            if char == ' ':
                i += 1
                continue
            
            if char == '(':
                tokens.append(('LPAREN', '('))
                i += 1
                continue
            
            if char == ')':
                tokens.append(('RPAREN', ')'))
                i += 1
                continue
            
            if char == '&':
                if i + 1 < length and expression[i + 1] == '&':
                    tokens.append(('AND', '&&'))
                    i += 2
                    continue
                else:
                    raise ValueError("Invalid character '&'")
            
            if char == '|':
                if i + 1 < length and expression[i + 1] == '|':
                    tokens.append(('OR', '||'))
                    i += 2
                    continue
                else:
                    raise ValueError("Invalid character '|'")
            
            if char == '!':
                tokens.append(('NOT', '!'))
                i += 1
                continue
            
            if char.isalpha() or char == '_':
                start = i
                while i < length and (expression[i].isalnum() or expression[i] == '_'):
                    i += 1
                name = expression[start:i]
                tokens.append(('NAME', name))
                continue
            
            raise ValueError(f"Unexpected character: {char}")

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
            val = self._parse_not(tokens)
            return not val
        
        return self._parse_primary(tokens)

    def _parse_primary(self, tokens: list) -> bool:
        if not tokens:
            raise ValueError("Unexpected end of expression")
        
        token_type, token_val = tokens[0]
        
        if token_type == 'LPAREN':
            tokens.pop(0)
            result = self._parse_or(tokens)
            if not tokens or tokens[0][0] != 'RPAREN':
                raise ValueError("Missing closing parenthesis")
            tokens.pop(0)
            return result
        
        if token_type == 'NAME':
            tokens.pop(0)
            name = token_val
            if name not in self.flags:
                raise ValueError(f"Unknown flag: {name}")
            return bool(self.flags[name])
        
        raise ValueError(f"Unexpected token: {token_val}")

if __name__ == '__main__':
    flags = {
        'A': True,
        'B': False,
        'C': True,
        'D': False
    }
    
    evaluator = FlagEvaluator(flags)
    
    expr1 = "A && B"
    result1 = evaluator.evaluate(expr1)
    print(result1)
    
    expr2 = "A || B"
    result2 = evaluator.evaluate(expr2)
    print(result2)
    
    expr3 = "!(A && B)"
    result3 = evaluator.evaluate(expr3)
    print(result3)
    
    expr4 = "A && (B || C)"
    result4 = evaluator.evaluate(expr4)
    print(result4)
    
    expr5 = "A || B && C"
    result5 = evaluator.evaluate(expr5)
    print(result5)