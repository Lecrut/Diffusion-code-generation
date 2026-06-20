class PropositionalLogicEvaluator:
    def __init__(self):
        self.operators = {'and', 'or', 'not'}

    def to_cnf(self, formula):
        stack = []
        output = ''
        i = 0
        while i < len(formula):
            if formula[i] == '(':
                stack.append('(')
                i += 1
            elif formula[i] in self.operators:
                while (stack and stack[-1] != '(' and 
                       self.precedence(stack[-1]) >= self.precedence(formula[i])):
                    output += stack.pop()
                stack.append(formula[i])
                i += 1
            elif formula[i] == ')':
                while stack and stack[-1] != '(':
                    output += stack.pop()
                stack.pop()
                i += 1
            else:
                while (i < len(formula) - 1 
                       and formula[i+1] not in self.operators):
                    i += 1
                output += formula[i]
                i += 1
        while stack:
            output += stack.pop()

        def apply_not(formula):
            if 'not' in formula:
                index = formula.index('not')
                return f"({formula[:index]}{self.apply_not(formula[index+3:])})"
            else:
                return formula

        def distribute_or_over_and(formula):
            if 'or' in formula and 'and' in formula:
                index_or = formula.find('or')
                left, right = formula[:index_or], formula[index_or + 2:]
                new_left = f"({distribute_or_over_and(left)}{self.distribute_or_over_and(right[1:-1])})"
                return distribute_or_over_and(new_left)
            else:
                return formula

        def remove_double_negation(formula):
            if 'not not' in formula:
                return formula.replace('not not', '')
            else:
                return formula

        output = apply_not(output)
        output = distribute_or_over_and(output)
        output = remove_double_negation(output)

        return set(output.split())

    def precedence(self, operator):
        if operator == 'or':
            return 1
        elif operator == 'and':
            return 2
        else:
            return 3

    def compare_formulas(self, formula1, formula2):
        cnf1 = self.to_cnf(formula1)
        cnf2 = self.to_cnf(formula2)
        return set(cnf1) == set(cnf2)

if __name__ == '__main__':
    evaluator = PropositionalLogicEvaluator()
    result = evaluator.compare_formulas('(A and B) or (C and D)', '(B and A) or (D and C)')
    print(result)