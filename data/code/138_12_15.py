class TruthTableGenerator:
    def generate_truth_table(self, expression, var1=None, var2=None):
        if not isinstance(expression, str) or len(expression) == 0:
            return "Error: Expression must be a non-empty string."
        
        inputs = [var1, var2] if var2 is not None else [var1]
        num_inputs = len(inputs)
        num_rows = 2 ** num_inputs
        table = []

        for i in range(num_rows):
            row = {}
            for j in range(num_inputs):
                if (i >> j) & 1:
                    row[f'a' + str(j)] = inputs[j]
                else:
                    row[f'a' + str(j)] = not inputs[j]
            
            result = eval(expression, {'__builtins__': None}, row)
            table.append({'a': row['a0'], 'b': row.get('a1', None), 'result': result})

        return table

if __name__ == '__main__':
    ttg = TruthTableGenerator()
    print(ttg.generate_truth_table('(a and b) or not a', var1=True, var2=False))
    print(ttg.generate_truth_table('not (a xor b)', var1=False, var2=True))