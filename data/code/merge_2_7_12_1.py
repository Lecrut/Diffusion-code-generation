import re
class LogicalParser:
    def __init__(self):
        self.tokens = []
    def tokenize(self, expression):
        if not isinstance(expression, str) or len(expression.strip()) == 0:
            raise ValueError("Invalid input type")
        tokens = []
        i = 0
        while i < len(expression):
            char = expression[i]
            if char in '()&!':
                tokens.append(char)
                i += 1
                continue
            elif re.match(r'[a-zA-Z_][a-zA-Z0-9_]*', char):
                j = i + 1
                while j < len(expression) and (expression[j].isalnum() or expression[j] == '_'):
                    j += 1
                tokens.append(expression[i:j])
                i = j
                continue
            elif char.isspace():
                i += 1
                continue
            else:
                raise ValueError(f"Invalid character '{char}' in expression")
        return tokens
    def validate_tokens(self, expr_str):
        self.tokens = []
        try:
            if not isinstance(expr_str, str) or len(expr_str.strip()) == 0:
                raise ValueError("Input must be a non-empty string")
        except ValueError:
            raise
        self.tokens = []
        i = 0
        while i < len(expr_str):
            char = expr_str[i]
            if char in '()&!':
                self.tokens.append(char)
                i += 1
            elif re.match(r'[a-zA-Z_][a-zA-Z0-9_]*', char):
                j = i + 1
                while j < len(expr_str) and (expr_str[j].isalnum() or expr_str[j] == '_'):
                    j += 1
                self.tokens.append(expr_str[i:j])
                i = j
            elif not char.isspace():
                raise ValueError(f"Invalid character '{char}' found")
        return self.tokens
    def parse(self, expression):
        tokens = self.tokenize(expression)
        if len(tokens) == 0:
            raise ValueError("Empty logical statement")
        return tokens
if __name__ == '__main__':
    parser = LogicalParser()
    test_cases = [
        "A",
        "not B",
        "C and D",
        "(E or F) and G"                                                                                                                                                                                                                                                                                                                                                                        
    ]
    for test in test_cases:
        try:
            result = parser.parse(test)
            print(f"Parsed '{test}': {result}")
        except ValueError as e:
            print(f"Error parsing '{test}': {e}")