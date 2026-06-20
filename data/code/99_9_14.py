import operator

class BooleanExpressionEvaluator:
    OPERATORS = {'AND': (2, operator.and_), 'OR': (1, operator.or_)}
    PRECEDENCE = {'NOT': 3, '(': 0, ')': 0}

    def evaluate(self, expression):
        tokens = self._tokenize(expression)
        return self._evaluate(tokens)

    def _tokenize(self, expression):
        tokens = []
        i = 0
        while i < len(expression):
            char = expression[i]
            if char.isspace():
                i += 1
                continue
            elif char.isalpha():
                j = i + 1
                while j < len(expression) and expression[j].isalpha():
                    j += 1
                tokens.append(expression[i:j])
                i = j
            else:
                tokens.append(char)
                i += 1
        return tokens

    def _evaluate(self, tokens):
        stack_operands = []
        stack_operators = []
        for token in tokens:
            if isinstance(token, bool):
                stack_operands.append(token)
            elif token == 'NOT':
                operand = stack_operands.pop()
                stack_operands.append(not operand)
            elif token in self.OPERATORS:
                while stack_operators and stack_operators[-1] != '(' and (self.PRECEDENCE[stack_operators[-1]] >= self.PRECEDENCE[token]):
                    operator = stack_operators.pop()
                    right_operand = stack_operands.pop()
                    left_operand = stack_operands.pop()
                    result = self.OPERATORS[operator][1](left_operand, right_operand)
                    stack_operands.append(result)
                stack_operators.append(token)
            elif token == '(':
                stack_operators.append(token)
            elif token == ')':
                while stack_operators[-1] != '(':
                    operator = stack_operators.pop()
                    right_operand = stack_operands.pop()
                    left_operand = stack_operands.pop()
                    result = self.OPERATORS[operator][1](left_operand, right_operand)
                    stack_operands.append(result)
                stack_operators.pop()
        while stack_operators:
            operator = stack_operators.pop()
            right_operand = stack_operands.pop()
            left_operand = stack_operands.pop()
            result = self.OPERATORS[operator][1](left_operand, right_operand)
            stack_operands.append(result)
        return stack_operands[0]
if __name__ == '__main__':
    evaluator = BooleanExpressionEvaluator()
    expression = 'NOT A AND B OR C'
    sample_values = {'A': True, 'B': False, 'C': True}
    result = evaluator.evaluate(expression)
    print(result)