class BooleanEvaluator:
    PRECEDENCE = {'NOT': 3, 'AND': 2, 'OR': 1, '(': 0}

    def check_precedence(self, expression_string):
        tokens = re.findall(r'\(|\)|\bAND\b|\bOR\b|\bNOT\b|\d+', expression_string)
        if not tokens:
            return "Error: Empty expression"
        output_order = []
        operator_stack = []
        for token in tokens:
            while operator_stack and self.PRECEDENCE[operator_stack[-1]] >= self.PRECEDENCE[token]:
                output_order.append(operator_stack.pop())
            operator_stack.append(token)
        while operator_stack:
            output_order.append(operator_stack.pop())
        return ' '.join(output_order)

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    expression = "NOT (A AND B) OR C"
    print(evaluator.check_precedence(expression))