class TruthTableGenerator:
    @staticmethod
    def generate_truth_table():
        variables = ['P', 'Q', 'R']
        num_rows = 2 ** len(variables)
        truth_table = []
        
        for i in range(num_rows):
            row = []
            for var in variables:
                bit = (i >> variables.index(var)) & 1
                row.append(bit == 1)
            truth_table.append(row)
        
        return truth_table

if __name__ == '__main__':
    generator = TruthTableGenerator()
    result = generator.generate_truth_table()
    print(result)