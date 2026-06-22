from functools import reduce
from operator import and_, or_

class FlagEvaluator:
    def __init__(self, flags):
        self.flags = flags

    def evaluate(self, expression):
        if not expression:
            return False
        tokens = self._tokenize(expression)
        if not tokens:
            return False
        return self._parse_or(tokens)

    def _tokenize(self, expr):
        tokens = []
        current = []
        for char in expr:
            if char == '(':
                if current:
                    tokens.append(''.join(current))
                    current = []
                tokens.append('(')
            elif char == ')':
                if current:
                    tokens.append(''.join(current))
                    current = []
                tokens.append(')')
            elif char in ('&', '|'):
                if current:
                    tokens.append(''.join(current))
                    current = []
                tokens.append(char)
            else:
                current.append(char)
        if current:
            tokens.append(''.join(current))
        return tokens

    def _parse_or(self, tokens):
        if not tokens:
            return False
        result = self._parse_and(tokens)
        while tokens and tokens[0] == '|':
            tokens.pop(0)
            if not tokens:
                break
            right = self._parse_and(tokens)
            result = result or right
        return result

    def _parse_and(self, tokens):
        if not tokens:
            return False
        result = self._parse_atom(tokens)
        while tokens and tokens[0] == '&':
            tokens.pop(0)
            if not tokens:
                break
            right = self._parse_atom(tokens)
            result = result and right
        return result

    def _parse_atom(self, tokens):
        if not tokens:
            return False
        token = tokens.pop(0)
        if token == '(':
            result = self._parse_or(tokens)
            if tokens and tokens[0] == ')':
                tokens.pop(0)
            return result
        if token in ('&', '|'):
            return False
        return self._resolve_flag(token)

    def _resolve_flag(self, name):
        name = name.strip()
        if not name:
            return False
        if name.startswith('!'):
            flag_name = name[1:]
            return not self.flags.get(flag_name, False)
        return self.flags.get(name, False)

def process_flags(flags, expression):
    evaluator = FlagEvaluator(flags)
    return evaluator.evaluate(expression)

if __name__ == '__main__':
    flags = {'A': True, 'B': False, 'C': True}
    expr = "A & B | C"
    result = process_flags(flags, expr)
    print(result)