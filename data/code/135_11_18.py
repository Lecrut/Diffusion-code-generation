import itertools

def evaluate_formula(formula, truth_values):
    if isinstance(formula, bool):
        return formula
    elif isinstance(formula, str):
        if formula == 'T':
            return True
        elif formula == 'F':
            return False
    elif isinstance(formula, tuple):
        operator, *operands = formula
        if operator == 'AND':
            return all((evaluate_formula(operand, truth_values) for operand in operands))
        elif operator == 'OR':
            return any((evaluate_formula(operand, truth_values) for operand in operands))
        elif operator == 'NOT':
            return not evaluate_formula(operands[0], truth_values)
    raise ValueError('Invalid formula')

def check_equivalence(expr1, expr2):
    if not (isinstance(expr1, str) and isinstance(expr2, str)):
        raise ValueError('Both expressions must be string representations of propositional logic formulas')
    variables = set()
    for expr in (expr1, expr2):
        stack = []
        for char in expr:
            if char.isalpha():
                variables.add(char)
            elif char == ')':
                while stack[-1] != '(':
                    stack.pop()
                stack.pop()
    variable_combinations = list(itertools.product([True, False], repeat=len(variables)))
    for truth_values in variable_combinations:
        truth_dict = {variable: value for variable, value in zip(variables, truth_values)}
        if evaluate_formula(expr1, truth_dict) != evaluate_formula(expr2, truth_dict):
            return False
    return True
if __name__ == '__main__':
    print(f'Test 1 (A AND B) vs (B AND A): {check_equivalence('(A AND B)', '(B AND A)')}')
    print(f'Test 2 ((A OR B) AND C) vs ((C AND B) OR A): {check_equivalence('((A OR B) AND C)', '((C AND B) OR A)')}')
    print(f'Test 3 (T) vs (F): {check_equivalence('T', 'F')}')