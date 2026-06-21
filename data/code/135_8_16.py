class PropositionalLogicEvaluator:
    def __init__(self):
        self.operators = {'&', '|', '!', '->', '<->'}
    
    def to_cnf(self, formula):
        formula = formula.replace(' ', '').replace(')', ' )')
        stack = []
        output = []
        for char in formula:
            if char not in self.operators and char != '(':
                output.append(char)
            elif char == '(':
                stack.append(char)
            elif char == ')':
                while stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()
            else:
                while (stack and stack[-1] != '(' and
                       self.get_precedence(char) <= self.get_precedence(stack[-1])):
                    output.append(stack.pop())
                stack.append(char)
        while stack:
            output.append(stack.pop())
        return ' '.join(output)
    
    def get_precedence(self, op):
        if op == '|' or op == '&':
            return 2
        elif op == '!':
            return 3
        elif op in ('->', '<->'):
            return 1
        else:
            return 0
    
    def compare_formulas(self, formula1, formula2):
        cnf1 = self.to_cnf(formula1).split()
        cnf2 = self.to_cnf(formula2).split()
        return set(cnf1) == set(cnf2)

if __name__ == '__main__':
    evaluator = PropositionalLogicEvaluator()
    result = evaluator.compare_formulas('(A & B) | C', '(C | A) & (B | A)')
    print(result)