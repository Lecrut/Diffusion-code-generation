import re

class BooleanEvaluator:
    PRECEDENCE = {'not': 3, 'and': 2, 'or': 1}

    def check_precedence(self, expression_string):
        tokens = re.findall('\\b\\w+\\b|\\(|\\)', expression_string)
        stack = []
        output = []
        for token in tokens:
            if token.isdigit():
                output.append(int(token))
            elif token in self.PRECEDENCE:
                while stack and stack[-1] != '(' and (self.PRECEDENCE[stack[-1]] >= self.PRECEDENCE[token]):
                    output.append(stack.pop())
                stack.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()
        while stack:
            output.append(stack.pop())
        return self._evaluate(output)

    def _evaluate(self, tokens):
        stack = []
        for token in tokens:
            if isinstance(token, int):
                stack.append(token)
            else:
                right = stack.pop()
                left = stack.pop()
                if token == 'not':
                    stack.append(not left)
                elif token == 'and':
                    stack.append(left and right)
                elif token == 'or':
                    stack.append(left or right)
        return stack[0]
if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    print(evaluator.check_precedence('not (1 and 0) or (1 and 1)'))
    print(evaluator.check_precedence('(2 or 3) and (4 or 5)'))
    print(evaluator.check_precedence('not (1 or 0)'))