class BooleanEvaluator:
    def __init__(self):
        self.precedence = {
            'or': 1,
            'and': 2,
            'not': 3
        }
        self.associativity = {
            'or': 'left',
            'and': 'left',
            'not': 'right'
        }

    def check_precedence(self, expression_string):
        if not expression_string or not expression_string.strip():
            raise ValueError("Empty expression")
        
        tokens = self._tokenize(expression_string)
        if not tokens:
            raise ValueError("No valid tokens")
        
        precedence_log = []
        self._evaluate_with_logging(tokens, precedence_log)
        
        return precedence_log

    def _tokenize(self, expression_string):
        tokens = []
        i = 0
        length = len(expression_string)
        
        while i < length:
            char = expression_string[i]
            
            if char.isspace():
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
            
            if char == 'n' and expression_string[i:i+3].lower() == 'not':
                tokens.append(('UNARY_NOT', 'not'))
                i += 3
                continue
            
            if char == 'a' and expression_string[i:i+3].lower() == 'and':
                tokens.append(('AND', 'and'))
                i += 3
                continue
            
            if char == 'o' and expression_string[i:i+2].lower() == 'or':
                tokens.append(('OR', 'or'))
                i += 2
                continue
            
            if char in ('0', '1', 'T', 'F', 't', 'f', 'T', 'F'):
                val = char.lower()
                if val in ('t', '1'):
                    tokens.append(('BOOL', True))
                else:
                    tokens.append(('BOOL', False))
                i += 1
                continue
            
            raise ValueError(f"Invalid character: {char}")
        
        return tokens

    def _evaluate_with_logging(self, tokens, log):
        if not tokens:
            return False, log
        
        result, log = self._parse_or(tokens, 0, log)
        return result, log

    def _parse_or(self, tokens, pos, log):
        left, pos = self._parse_and(tokens, pos, log)
        
        while pos < len(tokens) and tokens[pos][0] == 'OR':
            op = tokens[pos][1]
            pos += 1
            right, pos = self._parse_and(tokens, pos, log)
            log.append(('OR', op, left, right))
            left = left or right
        
        return left, pos

    def _parse_and(self, tokens, pos, log):
        left, pos = self._parse_not(tokens, pos, log)
        
        while pos < len(tokens) and tokens[pos][0] == 'AND':
            op = tokens[pos][1]
            pos += 1
            right, pos = self._parse_not(tokens, pos, log)
            log.append(('AND', op, left, right))
            left = left and right
        
        return left, pos

    def _parse_not(self, tokens, pos, log):
        if pos < len(tokens) and tokens[pos][0] == 'UNARY_NOT':
            op = tokens[pos][1]
            pos += 1
            operand, pos = self._parse_not(tokens, pos, log)
            log.append(('NOT', op, operand))
            return not operand, pos
        
        return self._parse_primary(tokens, pos, log)

    def _parse_primary(self, tokens, pos, log):
        if pos >= len(tokens):
            raise ValueError("Unexpected end of expression")
        
        token = tokens[pos]
        
        if token[0] == 'BOOL':
            return token[1], pos + 1
        
        if token[0] == 'LPAREN':
            pos += 1
            result, pos = self._parse_or(tokens, pos, log)
            if pos >= len(tokens) or tokens[pos][0] != 'RPAREN':
                raise ValueError("Missing closing parenthesis")
            pos += 1
            return result, pos
        
        raise ValueError(f"Unexpected token: {token}")

if __name__ == '__main__':
    evaluator = BooleanEvaluator()