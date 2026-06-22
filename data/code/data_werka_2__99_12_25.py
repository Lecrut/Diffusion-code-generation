class FlagEvaluator:
    def __init__(self, flags: dict):
        self.flags = flags

    def evaluate(self, expression: str) -> bool:
        if not isinstance(expression, str):
            raise ValueError("Expression must be a string")
        
        expression = expression.strip()
        if not expression:
            raise ValueError("Expression cannot be empty")
            
        tokens = self._tokenize(expression)
        if not tokens:
            raise ValueError("Invalid expression")
            
        result, _ = self._parse_or(tokens, 0)
        return result

    def _tokenize(self, expression: str) -> list:
        tokens = []
        i = 0
        length = len(expression)
        while i < length:
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
            elif char == '&' and i + 1 < length and expression[i+1] == '&':
                tokens.append('AND')
                i += 2
            elif char == '|' and i + 1 < length and expression[i+1] == '|':
                tokens.append('OR')
                i += 2
            elif char == '!' and i + 1 < length and expression[i+1] == '!':
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

    def _parse_or(self, tokens: list, pos: int) -> tuple:
        left, pos = self._parse_and(tokens, pos)
        while pos < len(tokens) and tokens[pos] == 'OR':
            pos += 1
            if pos >= len(tokens):
                raise ValueError("Unexpected end of expression")
            right, pos = self._parse_and(tokens, pos)
            if left:
                return True, pos
            left = right
        return left, pos

    def _parse_and(self, tokens: list, pos: int) -> tuple:
        left, pos = self._parse_not(tokens, pos)
        while pos < len(tokens) and tokens[pos] == 'AND':
            pos += 1
            if pos >= len(tokens):
                raise ValueError("Unexpected end of expression")
            right, pos = self._parse_not(tokens, pos)
            if not left:
                return False, pos
            left = right
        return left, pos

    def _parse_not(self, tokens: list, pos: int) -> tuple:
        if pos < len(tokens) and tokens[pos] == 'NOT':
            pos += 1
            if pos >= len(tokens):
                raise ValueError("Unexpected end of expression")
            val, pos = self._parse_not(tokens, pos)
            return not val, pos
        return self._parse_primary(tokens, pos)

    def _parse_primary(self, tokens: list, pos: int) -> tuple:
        if pos >= len(tokens):
            raise ValueError("Unexpected end of expression")
        
        token = tokens[pos]
        
        if token == '(':
            pos += 1
            val, pos = self._parse_or(tokens, pos)
            if pos >= len(tokens) or tokens[pos] != ')':
                raise ValueError("Missing closing parenthesis")
            pos += 1
            return val, pos
        
        if token in ('AND', 'OR', ')'):
            raise ValueError(f"Unexpected token: {token}")
            
        if token in self.flags:
            return bool(self.flags[token]), pos + 1
            
        raise ValueError(f"Unknown flag: {token}")

def process_flags(flags: dict, expression: str) -> bool:
    evaluator = FlagEvaluator(flags)
    return evaluator.evaluate(expression)

if __name__ == '__main__':
    flags = {
        'is_admin': True,
        'is_active': False,
        'has_permission': True,
        'is_expired': False,
        'is_locked': True
    }
    
    expr1 = "is_admin & is_active"
    result1 = process_flags(flags, expr1)
    print(result1)
    
    expr2 = "is_admin | is_active"