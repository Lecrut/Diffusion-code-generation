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
        result_stack = []
        operator_stack = []
        i = 0
        length = len(tokens)
        while i < length:
            token = tokens[i]
            if token == '(':
                operator_stack.append(token)
            elif token == ')':
                while operator_stack and operator_stack[-1] != '(':
                    op = operator_stack.pop()
                    val2 = result_stack.pop()
                    val1 = result_stack.pop()
                    res = self._apply_op(op, val1, val2)
                    result_stack.append(res)
                if not operator_stack:
                    raise ValueError("Mismatched parentheses")
                operator_stack.pop()
            elif token in operators:
                while (operator_stack and
                       operator_stack[-1] != '(' and
                       precedence_map.get(operator_stack[-1], 0) >= precedence_map[token]):
                    op = operator_stack.pop()
                    val2 = result_stack.pop()
                    val1 = result_stack.pop()
                    res = self._apply_op(op, val1, val2)
                    result_stack.append(res)
                operator_stack.append(token)
            elif token in ('True', 'False'):
                result_stack.append(token == 'True')
            else:
                raise ValueError(f"Unknown token: {token}")
            i += 1
        while operator_stack:
            op = operator_stack.pop()
            if op == '(':
                raise ValueError("Mismatched parentheses")
            if op == 'not':
                val = result_stack.pop()
                res = not val
                result_stack.append(res)
            else:
                val2 = result_stack.pop()
                val1 = result_stack.pop()
                res = self._apply_op(op, val1, val2)
                result_stack.append(res)
        if len(result_stack) != 1:
            raise ValueError("Invalid expression structure")
        return result_stack[0]

    def _tokenize(self, expression):
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
            elif expression[i:i+2] == 'or':
                tokens.append('or')
                i += 2
            elif expression[i:i+3] == 'and':
                tokens.append('and')
                i += 3
            elif expression[i:i+3] == 'not':
                tokens.append('not')
                i += 3
            elif expression[i:i+4] == 'True':
                tokens.append('True')
                i += 4
            elif expression[i:i+5] == 'False':
                tokens.append('False')
                i += 5
            else:
                raise ValueError(f"Unexpected character: {char}")
        return tokens

    def _apply_op(self, op, val1, val2):
        if op == 'and':
            return val1 and val2
        elif op == 'or':
            return val1 or val2
        return False

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    expr1 = "True and False or True"
    print(evaluator.check_precedence(expr1))
    expr2 = "not True"
    print(evaluator.check_precedence(expr2))