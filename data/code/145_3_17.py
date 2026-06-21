class BooleanEvaluator:

    def evaluate(self, expression):
        stack = []
        operators = set(['&', '|', '^'])
        for char in expression:
            if char.isdigit():
                stack.append(int(char))
            elif char in operators:
                b = stack.pop()
                a = stack.pop()
                if char == '&':
                    stack.append(a & b)
                elif char == '|':
                    stack.append(a | b)
                elif char == '^':
                    stack.append(a ^ b)
        return stack[0]
if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    result = evaluator.evaluate('1&0|1^0')
    print(result)