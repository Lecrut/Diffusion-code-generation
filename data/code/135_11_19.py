class PropositionalEquivalenceChecker:

    def evaluate_expression(self, expr, truth_assignment):
        if isinstance(expr, bool):
            return expr
        elif isinstance(expr, str):
            if expr == 'T':
                return True
            elif expr == 'F':
                return False
            else:
                raise ValueError('Invalid expression format')
        elif isinstance(expr, list) and all((isinstance(subexpr, (bool, str)) for subexpr in expr)):
            if len(expr) != 3 or expr[1] not in ['&', '|', '->']:
                raise ValueError('Invalid binary operation')
            left = self.evaluate_expression(expr[0], truth_assignment)
            right = self.evaluate_expression(expr[2], truth_assignment)
            if expr[1] == '&':
                return left and right
            elif expr[1] == '|':
                return left or right
            elif expr[1] == '->':
                return not left or right
        else:
            raise ValueError('Invalid expression format')

    def are_equivalent(self, expr1, expr2):
        truth_values = {f'p{i}': val for i in range(3) for val in [True, False]}
        results = []
        for _ in range(8):
            current_assignment = dict(truth_values)
            result1 = self.evaluate_expression(expr1, current_assignment)
            result2 = self.evaluate_expression(expr2, current_assignment)
            results.append((result1, result2))
            for p in truth_values:
                if truth_values[p]:
                    truth_values[p] = False
                else:
                    truth_values[p] = True
        return all((result[0] == result[1] for result in results))
if __name__ == '__main__':
    checker = PropositionalEquivalenceChecker()
    expr1 = ['p0', '&', 'p1']
    expr2 = ['p2', '|', '->', 'p0', 'p1']
    print(f'Test 1 (expr1 vs expr2): {checker.are_equivalent(expr1, expr2)}')