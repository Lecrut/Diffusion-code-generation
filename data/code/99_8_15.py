class BooleanEvaluator:
    def check_precedence(self, expression_string):
        tokens = self._tokenize(expression_string)
        if not tokens:
            raise ValueError("Empty expression")
        result, steps = self._parse_or(tokens, 0)
        return steps

    def _tokenize(self, expr):
        tokens = []
        i = 0
        length = len(expr)
        while i < length:
            char = expr[i]
            if char.isspace():
                i += 1
                continue
            if char == '(':
                tokens.append(('LPAREN', '('))
                i += 1
            elif char == ')':
                tokens.append(('RPAREN', ')'))
                i += 1
            elif char in ('!', 'not'):
                if char == '!':
                    tokens.append(('NOT', 'not'))
                else:
                    tokens.append(('NOT', 'not'))
                i += 1
            elif char in ('&', 'and'):
                if char == '&':
                    tokens.append(('AND', 'and'))
                else:
                    tokens.append(('AND', 'and'))
                i += 1
            elif char in ('|', 'or'):
                if char == '|':
                    tokens.append(('OR', 'or'))
                else:
                    tokens.append(('OR', 'or'))
                i += 1
            elif char in ('0', '1'):
                tokens.append(('BOOL', char == '1'))
                i += 1
            elif char.isalpha():
                word = []
                while i < length and expr[i].isalpha():
                    word.append(expr[i])
                    i += 1
                word_str = ''.join(word).lower()
                if word_str in ('true', '1'):
                    tokens.append(('BOOL', True))
                elif word_str in ('false', '0'):
                    tokens.append(('BOOL', False))
                else:
                    raise ValueError(f"Unknown identifier: {word_str}")
            else:
                raise ValueError(f"Unexpected character: {char}")
        return tokens

    def _parse_or(self, tokens, pos):
        pos, left, steps = self._parse_and(tokens, pos)
        current_steps = []
        if pos < len(tokens) and tokens[pos][0] == 'OR':
            current_steps.append(('Evaluated OR precedence', left, tokens[pos][1]))
            pos += 1
            right, right_steps = self._parse_or(tokens, pos)
            current_steps.extend(right_steps)
            result = left or right
            current_steps.append(('Result of OR', result))
            return result, current_steps
        return left, current_steps

    def _parse_and(self, tokens, pos):
        pos, left, steps = self._parse_not(tokens, pos)
        current_steps = []
        if pos < len(tokens) and tokens[pos][0] == 'AND':
            current_steps.append(('Evaluated AND precedence', left, tokens[pos][1]))
            pos += 1
            right, right_steps = self._parse_and(tokens, pos)
            current_steps.extend(right_steps)
            result = left and right
            current_steps.append(('Result of AND', result))
            return result, current_steps
        return left, current_steps

    def _parse_not(self, tokens, pos):
        if pos < len(tokens) and tokens[pos][0] == 'NOT':
            pos += 1
            operand, operand_steps = self._parse_not(tokens, pos)
            result = not operand
            steps = operand_steps + [('Evaluated NOT precedence', operand, 'not'), ('Result of NOT', result)]
            return result, steps
        return self._parse_primary(tokens, pos)

    def _parse_primary(self, tokens, pos):
        if pos < len(tokens):
            token_type, token_val = tokens[pos]
            if token_type == 'BOOL':
                return token_val, []
            elif token_type == 'LPAREN':
                pos += 1
                result, steps = self._parse_or(tokens, pos)
                if pos < len(tokens) and tokens[pos][0] == 'RPAREN':
                    pos += 1
                    return result, steps
                else:
                    raise ValueError("Missing closing parenthesis")
            else:
                raise ValueError(f"Unexpected token: {token_val}")
        raise ValueError("Unexpected end of expression")

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    expr = "True and False or not True"
    print(evaluator.check_precedence(expr))