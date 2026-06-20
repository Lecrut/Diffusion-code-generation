def evaluate_boolean_expression(expression):

    def parse_and_evaluate(tokens):
        values = []
        ops = []
        precedence = {'not': 3, 'and': 2, 'or': 1}

        def apply_operator():
            right = values.pop()
            left = values.pop()
            op = ops.pop()
            if op == 'not':
                values.append(not right)
            elif op == 'and':
                values.append(left and right)
            elif op == 'or':
                values.append(left or right)
        i = 0
        while i < len(tokens):
            token = tokens[i]
            if token in precedence:
                while ops and precedence[ops[-1]] >= precedence[token]:
                    apply_operator()
                ops.append(token)
            else:
                values.append(eval(token))
            i += 1
        while ops:
            apply_operator()
        return values.pop()

    def tokenize(expression):
        tokens = []
        i = 0
        while i < len(expression):
            if expression[i] == '(':
                tokens.append('(')
            elif expression[i] == ')':
                tokens.append(')')
            elif expression[i].isalnum() or expression[i] in ' not and or ()':
                j = i + 1
                while j < len(expression) and (expression[j].isalnum() or expression[j] in 'not and or'):
                    j += 1
                token = expression[i:j]
                tokens.append(token)
                i = j - 1
            i += 1
        return tokens
    return parse_and_evaluate(tokenize(expression))
if __name__ == '__main__':
    print(evaluate_boolean_expression('True and False or not True'))
    print(evaluate_boolean_expression(not (False or True) and True))
    print(evaluate_boolean_expression(True and (not (False and True))))
    print(evaluate_boolean_expression((True or False) and (not False)))