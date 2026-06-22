class LogicalFlagEvaluator:
    def __init__(self, flags: dict):
        self.flags = flags

    def evaluate(self, expression: str) -> bool:
        expression = expression.strip()
        if not expression:
            raise ValueError("Empty expression")
        
        tokens = self._tokenize(expression)
        if not tokens:
            raise ValueError("No tokens found")
        
        result = self._parse_or(tokens)
        if not isinstance(result, bool):
            raise ValueError("Invalid expression structure")
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
                tokens.append('(')
                i += 1
            elif char == ')':
                tokens.append(')')
                i += 1
            elif char == '&' and i + 1 < length and expression[i + 1] == '&':
                tokens.append('AND')
                i += 2
            elif char == '|' and i + 1 < length and expression[i + 1] == '|':
                tokens.append('OR')
                i += 2
            elif char == '!' and i + 1 < length and expression[i + 1] == '!':
                tokens.append('NOT')
                i += 2
            elif char.isalpha() or char == '_':
                start = i
                while i < length and (expression[i].isalnum() or expression[i] == '_'):
                    i += 1
                tokens.append(expression[start:i])
            else:
                raise ValueError(f"Unexpected character: {char}")
        return tokens

    def _parse_or(self, tokens: list) -> bool:
        left = self._parse_and(tokens)
        while tokens and tokens[0] == 'OR':
            tokens.pop(0)
            right = self._parse_and(tokens)
            if left is True:
                return True
            left = right
        return left

    def _parse_and(self, tokens: list) -> bool:
        left = self._parse_not(tokens)
        while tokens and tokens[0] == 'AND':
            tokens.pop(0)
            right = self._parse_not(tokens)
            if left is False:
                return False
            left = right
        return left

    def _parse_not(self, tokens: list) -> bool:
        if tokens and tokens[0] == 'NOT':
            tokens.pop(0)
            val = self._parse_not(tokens)
            return not val
        return self._parse_primary(tokens)

    def _parse_primary(self, tokens: list) -> bool:
        if not tokens:
            raise ValueError("Unexpected end of expression")
        
        token = tokens.pop(0)
        
        if token == '(':
            result = self._parse_or(tokens)
            if not tokens or tokens[0] != ')':
                raise ValueError("Missing closing parenthesis")
            tokens.pop(0)
            return result
        
        if token in ('AND', 'OR', ')'):
            raise ValueError(f"Unexpected token: {token}")
        
        if token in self.flags:
            return bool(self.flags[token])
        
        raise ValueError(f"Unknown flag: {token}")

if __name__ == '__main__':
    flags = {
        'A': True,
        'B': False,
        'C': True,
        'D': False,
        'E': True
    }
    
    evaluator = LogicalFlagEvaluator(flags)
    
    expr1 = "A & B | C"
    result1 = evaluator.evaluate(expr1)
    print(result1)
    
    expr2 = "!A & (B | C)"
    result2 = evaluator.evaluate(expr2)
    print(result2)
    
    expr3 = "A | B & C | D"
    result3 = evaluator.evaluate(expr3)
    print(result3)
    
    expr4 = "!(A & B)"
    result4 = evaluator.evaluate(expr4)
    print(result4)