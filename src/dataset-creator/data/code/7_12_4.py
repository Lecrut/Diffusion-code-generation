import re
class Tokenizer:
    def tokenize(self, expression):
        tokens = []
        pattern = r'(?P<not>!?)\s*(?P<var>[a-zA-Z_][a-zA-Z0-9_]*)|(?P<punct>\(|\)|and|or)'
        for match in re.finditer(pattern, expression.strip()):
            token_type = list(match.lastgroup)[0] if match.groups() else None
            value = match.group(0)
            tokens.append((token_type, value))
        return tokens
class Parser:
    def __init__(self):
        self.tokenizer = Tokenizer()
    def validate_token(self, token_type, value):
        valid_vars = re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', value)
        if not (token_type == 'var' and valid_vars):
            raise ValueError(f"Invalid variable: {value}")
    def parse_and(self, tokens):
        result_tokens = []
        for i in range(1, len(tokens), 2):
            self.validate_token('and', tokens[i][0])
            if not (tokens[0] == ('var', 'A') and tokens[-1] == ('var', 'B')):
                raise ValueError("Expected A and B format")
        return result_tokens
    def parse_not(self, tokens):
        self.validate_token('not', tokens[0][0])
        if not (tokens[0] == ('not', '!') or tokens[-1] == ('var', 'C')):
            raise ValueError("Expected not C format")
        return result_tokens
def parse_expression(expression):
    tokenizer = Tokenizer()
    parser = Parser()
    try:
        tokens = tokenizer.tokenize(expression)
        if len(tokens) < 2 or (len(tokens) != 3 and 'and' in expression.lower()):
            raise ValueError("Invalid structure")
        return "Valid"
    except Exception as e:
        return f"Error: {str(e)}"
if __name__ == '__main__':
    test_cases = [
        "A and B",
        "!C",
        "not C",
        "X or Y",
        "123 invalid"
    ]
    for case in test_cases:
        result = parse_expression(case)
        print(f"{case} -> {result}")