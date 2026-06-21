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
        i = 0
        length = len(expression)
        
        while i < length:
            char = expression[i]
            
            if char.isspace():
                i += 1
                continue
            
            if char == '(':
                tokens.append(('LPAREN', '('))
                i += 1
            elif char == ')':
                tokens.append(('RPAREN', ')'))
                i += 1
            elif char == '&' and i + 1 < length and expression[i + 1] == '&':
                tokens.append(('AND', '&&'))
                i += 2
            elif char == '|' and i + 1 < length and expression[i + 1] == '|':
                tokens.append(('OR', '||'))
                i += 2
            elif char == '!' and i + 1 < length and expression[i + 1] == '!':
                tokens.append(('NOT', '!!'))
                i += 2
            elif char == '!':
                tokens.append(('NOT', '!'))
                i += 1
            elif char.isalpha() or char == '_':
                start = i
                while i < length and (expression[i].isalnum() or expression[i] == '_'):
                    i += 1
                name = expression[start:i]
                value = self.flags.get(name, False)
                tokens.append(('FLAG', name, value))
            else:
                raise ValueError(f"Unexpected character: {char}")
        
        return tokens

    def _parse_or(self, tokens):
        result = self._parse_and(tokens)
        
        while tokens and tokens[0][0] == 'OR':
            tokens.pop(0)
            right = self._parse_and(tokens)
            if result:
                return True
            result = right
        
        return result

    def _parse_and(self, tokens):
        result = self._parse_not(tokens)
        
        while tokens and tokens[0][0] == 'AND':
            tokens.pop(0)
            right = self._parse_not(tokens)
            if not result:
                return False
            result = right
        
        return result

    def _parse_not(self, tokens):
        if tokens and tokens[0][0] == 'NOT':
            tokens.pop(0)
            operand = self._parse_not(tokens)
            return not operand
        
        return self._parse_primary(tokens)

    def _parse_primary(self, tokens):
        if not tokens:
            raise ValueError("Unexpected end of expression")
        
        token = tokens[0]
        
        if token[0] == 'FLAG':
            tokens.pop(0)
            return token[2]
        
        if token[0] == 'LPAREN':
            tokens.pop(0)
            result = self._parse_or(tokens)
            if not tokens or tokens[0][0] != 'RPAREN':
                raise ValueError("Missing closing parenthesis")
            tokens.pop(0)
            return result
        
        raise ValueError(f"Unexpected token: {token}")

if __name__ == '__main__':
    flags = {
        'A': True,
        'B': False,
        'C': True,
        'D': False,
        'E': True
    }
    
    evaluator = FlagEvaluator(flags)
    
    result1 = evaluator.evaluate("A && B || C")
    print(result1)
    
    result2 = evaluator.evaluate("!(A && B) && C")
    print(result2)
    
    result3 = evaluator.evaluate("A || B && C || D")
    print(result3)
    
    result4 = evaluator.evaluate("!!A")
    print(result4)
    
    result5 = evaluator.evaluate("(A || B) && (C || D)")
    print(result5)