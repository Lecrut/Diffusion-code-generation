import re
class Tokenizer:
    def tokenize(self, expression):
        tokens = []
        pattern = r'(\(|\)|and|not|[a-zA-Z]+)'
        matches = re.findall(pattern, expression)
        for match in matches:
            if match == '(':
                tokens.append('LPAREN')
            elif match == ')':
                tokens.append('RPAREN')
            elif match in ('and', 'or'):
                tokens.append(match.lower())
            elif match not in ('not',):
                tokens.append(('VAR', match))
            else:
                tokens.append(('NOT', None))
        return tokens
class Parser:
    def __init__(self, tokenizer):
        self.tokenizer = tokenizer
        self.tokens = []
    def parse(self, expression):
        try:
            self.tokens = self.tokenizer.tokenize(expression)
            if not self.tokens or len(self.tokens) == 1 and self.tokens[0] != 'LPAREN':
                raise ValueError("Invalid logical statement structure")
            result = self.parse_expression()
            return result, True
        except Exception as e:
            return None, False
    def parse_expression(self):
        left_val = self.parse_term()
        if not left_val or len(left_val) != 1:
            raise ValueError("Invalid expression structure")
        while self.tokens and self.tokens[0] in ('and', 'or'):
            op_token = self.tokens.pop(0).lower()
            right_val = self.parse_term()
            if not right_val or len(right_val) != 1:
                raise ValueError("Invalid expression structure")
            left_val.append((op_token, right_val[0]))
        return left_val
    def parse_term(self):
        term_tokens = []
        while self.tokens and self.tokens[0] in ('VAR', 'NOT'):
            token_type = self.tokens.pop(0)[0] if isinstance(self.tokens[0], tuple) else None
            if token_type == 'NOT':
                next_token = self.tokens.pop(0)
                if not (next_token and next_token[0] in ('VAR',)):
                    raise ValueError("Invalid operand after NOT")
                term_tokens.append(('NOT', next_token))
            elif token_type == 'VAR':
                var_name = self.tokens.pop(0)[1]
                if len(var_name) != 1:
                    raise ValueError(f"Variable name must be a single character, got '{var_name}'")
                term_tokens.append(('VAR', var_name))
        return term_tokens
def evaluate(expression):
    tokenizer = Tokenizer()
    parser = Parser(tokenizer)
    result, success = parser.parse(expression)
    if not success:
        raise ValueError("Failed to parse expression")
    variables = {}
    for token in result[0]:
        var_name = None
        if isinstance(token, tuple):
            op_type, val_token = token
            if op_type == 'VAR':
                var_name = val_token[1]
            elif op_type == 'NOT':
                next_op = parser.parse_term()
                for sub_token in next_op:
                    if isinstance(sub_token, tuple) and sub_token[0] == 'VAR':
                        var_name = sub_token[1][1]
        variables[var_name] = True
    return result
if __name__ == '__main__':
    test_cases = [
        "A",
        "not B",
        "(C and D)",
        "E or F"
    ]
    for case in test_cases:
        try:
            res, ok = evaluate(case)
            print(f"{case}: {res}, Success")
        except Exception as e:
            print(f"{case}: Error - {e}")