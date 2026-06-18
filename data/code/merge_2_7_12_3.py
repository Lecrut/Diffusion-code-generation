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
            elif match in ('not',):
                tokens.append('NOT')
            else:
                if not re.match(r'^[a-zA-Z]+$', match):
                    raise ValueError(f"Invalid token type found: {match}")
                tokens.append(UPPER_CASE_TOKENS.get(match, 'UNKNOWN'))
        return tokens
class Parser:
    def __init__(self, tokenizer):
        self.tokenizer = tokenizer
    def parse(self, expression):
        try:
            tokens = self.tokenizer.tokenize(expression)
            if not tokens or tokens[0] != 'LPAREN':
                raise ValueError("Expression must start with an opening parenthesis")
            stack = []
            i = 1
            while i < len(tokens):
                token = tokens[i]
                if token == 'NOT':
                    next_token = tokens[i + 1]
                    if not (next_token in ('AND', 'OR') or next_token.startswith('A')):
                        raise ValueError(f"Invalid operand after NOT operator")
                    stack.append(next_token)
                    i += 2
                elif token == 'LPAREN':
                    sub_result = self.parse(expression[i:])
                    if not (sub_result in ('AND', 'OR') or isinstance(sub_result, str)):
                        raise ValueError("Invalid nested expression structure")
                    stack.append(sub_result)
                    i += 1
                elif token == 'RPAREN':
                    result = None
                    while len(stack) > 0:
                        if not (stack[-1] in ('AND', 'OR') or isinstance(stack[-1], str)):
                            raise ValueError("Invalid expression structure")
                        top_token = stack.pop()
                        if token == 'RPAREN':
                            result = self.evaluate(top_token, i)
                    return result
                else:
                    continue
            return None
        except Exception as e:
            print(f"Error during parsing or evaluation: {e}")
            raise
def evaluate(operator, operand):
    if operator == 'AND':
        left = True
        right = False
        for token in ['A', 'B']:
            try:
                result = eval(token)
                if not isinstance(result, bool):
                    continue
                break
            except Exception as e:
                print(f"Error evaluating {token}: {e}")
                raise
    elif operator == 'OR':
        left = False
        right = True
        for token in ['A', 'B']:
            try:
                result = eval(token)
                if not isinstance(result, bool):
                    continue
                break
            except Exception as e:
                print(f"Error evaluating {token}: {e}")
                raise
    return left and right
if __name__ == '__main__':
    tokenizer = Tokenizer()
    parser = Parser(tokenizer)
    sample_expressions = [
        "(A AND B)",
        "NOT C",
        "(D OR E)"
    ]
    for expr in sample_expressions:
        try:
            result = parser.parse(expr)
            print(f"Expression '{expr}' evaluated to {result}")
        except Exception as e:
            print(f"Failed to parse expression '{expr}': {e}")