import itertools

class TruthTableGenerator:
    def generate_truth_table(self, formula):
        variables = set()
        for char in formula:
            if char.isalpha() and not char.isdigit():
                variables.add(char)
        
        n = len(variables)
        header = list(variables) + ['Result']
        truth_table = [header]
        
        for combination in itertools.product([False, True], repeat=n):
            row = list(map(str, combination))
            result = eval(formula, {'A': combination[0], 'B': combination[1], 'C': combination[2]})
            row.append(str(result))
            truth_table.append(row)
        
        return truth_table

if __name__ == '__main__':
    generator = TruthTableGenerator()
    formula = "(A AND B) OR (NOT C)"
    table = generator.generate_truth_table(formula)
    for row in table:
        print(" | ".join(row))