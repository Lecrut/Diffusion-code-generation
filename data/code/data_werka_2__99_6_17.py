from typing import List, Tuple, Union
import re

class BooleanExpressionAnalyzer:

    def __init__(self, expression: str):
        self.original_expression = expression
        self.tokens = self._tokenize(expression)
        self.precedence_rules = {'NOT': 3, 'AND': 2, 'OR': 1}
        self.result = self._evaluate(self.tokens)

    def _tokenize(self, expression: str) -> List[Tuple[str, Union[str, bool]]]:
        cleaned = expression.replace(' ', '')
        if not cleaned:
            raise ValueError('Empty expression')
        pattern = '\\b(AND|OR|NOT|TRUE|FALSE)\\b|[\\(\\)]'
        matches = re.finditer(pattern, cleaned, re.IGNORECASE)
        tokens = []
        for match in matches:
            word = match.group(1)
            if word.upper() == 'TRUE':
                tokens.append(('VAL', True))
            elif word.upper() == 'FALSE':
                tokens.append(('VAL', False))
            elif word.upper() in ('AND', 'OR', 'NOT'):
                tokens.append(('OP', word.upper()))
            else:
                tokens.append(('PAREN', word))
        if len(tokens) == 0:
            raise ValueError('No valid tokens found')
        return tokens

    def _evaluate(self, tokens: List[Tuple[str, Union[str, bool]]]) -> bool:
        if not tokens:
            raise ValueError('No tokens to evaluate')

        def parse_or(index):
            left, index = parse_and(index)
            while index < len(tokens) and tokens[index] == ('OP', 'OR'):
                index += 1
                right, index = parse_and(index)
                left = left or right
            return (left, index)

        def parse_and(index):
            left, index = parse_not(index)
            while index < len(tokens) and tokens[index] == ('OP', 'AND'):
                index += 1
                right, index = parse_not(index)
                left = left and right
            return (left, index)

        def parse_not(index):
            if index < len(tokens) and tokens[index] == ('OP', 'NOT'):
                index += 1
                val, index = parse_not(index)
                return (not val, index)
            return parse_paren(index)

        def parse_paren(index):
            if index < len(tokens) and tokens[index] == ('PAREN', '('):
                index += 1
                val, index = parse_or(index)
                if index >= len(tokens) or tokens[index] != ('PAREN', ')'):
                    raise ValueError('Mismatched parentheses')
                index += 1
                return (val, index)
            if index >= len(tokens):
                raise ValueError('Unexpected end of expression')
            val_type, val = tokens[index]
            if val_type != 'VAL':
                raise ValueError(f'Expected value, got {val_type}')
            return (val, index + 1)
        result, end_index = parse_or(0)
        if end_index != len(tokens):
            raise ValueError('Unexpected tokens at end of expression')
        return result
if __name__ == '__main__':
    analyzer = BooleanExpressionAnalyzer('TRUE AND FALSE')
    print(analyzer.result)
    analyzer2 = BooleanExpressionAnalyzer('(TRUE OR FALSE) AND NOT FALSE')
    print(analyzer2.result)
    analyzer3 = BooleanExpressionAnalyzer('NOT (TRUE AND FALSE)')
    print(analyzer3.result)