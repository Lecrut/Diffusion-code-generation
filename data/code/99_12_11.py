class BooleanEvaluator:
    def check_precedence(self, expression_string):
        tokens = re.findall(r'\(|\)|\bAND\b|\bOR\b|\bNOT\b|\d+|\s+', expression_string)
        if not tokens:
            return "Error: Empty expression"
        tokens_processed = [token.strip() for token in tokens if token.strip()]
        if not tokens_processed:
            return "Error: Could not parse expression"

        precedence_map = {
            'NOT': 3,
            'AND': 2,
            'OR': 1
        }

        stack_operands = []
        stack_operators = []

        for token in tokens_processed:
            if token.isdigit() or (token == 'true' or token == 'false'):
                stack_operands.append(token)
            elif token in precedence_map:
                while stack_operators and stack_operators[-1] != '(' and precedence_map[token] <= precedence_map[stack_operators[-1]]:
                    self.process_operator(stack_operands, stack_operators)
                stack_operators.append(token)
            elif token == '(':
                stack_operators.append(token)
            elif token == ')':
                while stack_operators and stack_operators[-1] != '(':
                    self.process_operator(stack_operands, stack_operators)
                if stack_operators and stack_operators[-1] == '(':
                    stack_operators.pop()

        while stack_operators:
            self.process_operator(stack_operands, stack_operators)

        return stack_operands[0]

    def process_operator(self, stack_operands, stack_operators):
        operator = stack_operators.pop()
        right = stack_operands.pop()
        left = stack_operands.pop()
        
        if operator == 'NOT':
            result = self.evaluate_not(right)
        elif operator == 'AND':
            result = self.evaluate_and(left, right)
        elif operator == 'OR':
            result = self.evaluate_or(left, right)

        stack_operands.append(result)

    def evaluate_not(self, operand):
        return not bool(operand.lower() == 'true')

    def evaluate_and(self, left, right):
        return bool(left.lower() == 'true') and bool(right.lower() == 'true')

    def evaluate_or(self, left, right):
        return bool(left.lower() == 'true') or bool(right.lower() == 'true')

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    print(evaluator.check_precedence("NOT (TRUE AND FALSE) OR TRUE"))