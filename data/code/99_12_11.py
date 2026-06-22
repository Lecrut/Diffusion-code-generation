class LogicalFlagEvaluator:
    def __init__(self, flags):
        if not isinstance(flags, dict):
            raise ValueError("Flags must be a dictionary")
        self.flags = {k: bool(v) for k, v in flags.items()}

    def evaluate(self, expression):
        if not isinstance(expression, str):
            raise ValueError("Expression must be a string")
        if not expression:
            raise ValueError("Expression cannot be empty")
        
        tokens = self._tokenize(expression)
        if not tokens:
            raise ValueError("Invalid expression")
        
        result = self._parse_or(tokens)
        if not isinstance(result, bool):
            raise ValueError("Expression did not resolve to a boolean")
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
            elif char == '!':
                tokens.append(('NOT', '!'))
                i += 1
            elif char.isalpha() or char == '_':
                start = i
                while i < length and (expression[i].isalnum() or expression[i] == '_'):
                    i += 1
                tokens.append(('FLAG', expression[start:i]))
            else:
                raise ValueError(f"Unexpected character: {char}")
        return tokens

    def _parse_or(self, tokens):
        left = self._parse_and(tokens)
        while tokens and tokens[0][0] == 'OR':
            tokens.pop(0)
            right = self._parse_and(tokens)
            if left is True:
                return True
            left = right
        return left

    def _parse_and(self, tokens):
        left = self._parse_not(tokens)
        while tokens and tokens[0][0] == 'AND':
            tokens.pop(0)
            right = self._parse_not(tokens)
            if left is False:
                return False
            left = right
        return left

    def _parse_not(self, tokens):
        if tokens and tokens[0][0] == 'NOT':
            tokens.pop(0)
            val = self._parse_not(tokens)
            return not val
        return self._parse_primary(tokens)

    def _parse_primary(self, tokens):
        if not tokens:
            raise ValueError("Unexpected end of expression")
        
        token_type, token_val = tokens[0]
        
        if token_type == 'FLAG':
            tokens.pop(0)
            if token_val not in self.flags:
                raise ValueError(f"Unknown flag: {token_val}")
            return self.flags[token_val]
        
        if token_type == 'LPAREN':
            tokens.pop(0)
            result = self._parse_or(tokens)
            if not tokens or tokens[0][0] != 'RPAREN':
                raise ValueError("Missing closing parenthesis")
            tokens.pop(0)
            return result
        
        raise ValueError(f"Unexpected token: {token_val}")

if __name__ == '__main__':
    flags = {
        'is_admin': True,
        'is_active': False,
        'has_permission': True,
        'is_verified': False
    }
    
    evaluator = LogicalFlagEvaluator(flags)
    
    expr1 = "is_admin && is_active"
    res1 = evaluator.evaluate(expr1)
    print(res1)
    
    expr2 = "is_admin || is_active"
    res2 = evaluator.evaluate(expr2)
    print(res2)
    
    expr3 = "!is_verified && (is_admin || is_active)"
    res3 = evaluator.evaluate(expr3)
    print(res3)
    
    expr4 = "is_admin && (is_active || has_permission)"
    res4 = evaluator.evaluate(expr4)
    print(res4)