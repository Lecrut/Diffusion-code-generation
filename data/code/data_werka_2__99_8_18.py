class BooleanEvaluator:
    def check_precedence(self, expression_string):
        expression_string = expression_string.strip()
        if not expression_string:
            raise ValueError("Empty expression")
        tokens = self._tokenize(expression_string)
        if not tokens:
            raise ValueError("No tokens found")
        precedence_map = {
            '(': 0,
            ')': 0,
            'or': 1,
            'and': 2,
            'not': 3,
        }
        operators = ['or', 'and', 'not']
        results = []
        stack = []
        for token in tokens:
            if token in operators:
                while stack and stack[-1] != '(' and precedence_map[stack[-1]] >= precedence_map[token]:
                    results.append(stack.pop())
                stack.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    results.append(stack.pop())
                stack.pop()
            else:
                results.append(token)
        while stack:
            results.append(stack.pop())
        return results

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
                tokens.append('(')
                i += 1
            elif char == ')':
                tokens.append(')')
                i += 1
            elif char == 'n' and expression_string[i:i+3] == 'not':
                tokens.append('not')
                i += 3
            elif char == 'a' and expression_string[i:i+3] == 'and':
                tokens.append('and')
                i += 3
            elif char == 'o' and expression_string[i:i+2] == 'or':
                tokens.append('or')
                i += 2
            elif char in ('T', 't') and expression_string[i:i+4].lower() == 'true':
                tokens.append('True')
                i += 4
            elif char in ('F', 'f') and expression_string[i:i+5].lower() == 'false':
                tokens.append('False')
                i += 5
            else:
                raise ValueError(f"Unknown character: {char}")
        return tokens

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    expression = "True and False or not True"
    result = evaluator.check_precedence(expression)
    print(result)
    expression2 = "not (True and False)"
    result2 = evaluator.check_precedence(expression2)
    print(result2)
    expression3 = "True or False and True"
    result3 = evaluator.check_precedence(expression3)
    print(result3)