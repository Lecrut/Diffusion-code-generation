class TruthTableGenerator:
    def __init__(self, variables=None):
        if variables is None:
            variables = ['A', 'B', 'C']
        self.variables = variables
        self.num_vars = len(variables)
        self.rows = 2 ** self.num_vars

    def generate(self):
        header = ' | '.join(self.variables)
        print(header)
        print('-' * len(header))
        for i in range(self.rows):
            values = []
            for j in range(self.num_vars):
                bit = (i >> (self.num_vars - 1 - j)) & 1
                values.append(str(bit))
            row_str = ' | '.join(values)
            print(row_str)
        return self.rows

if __name__ == '__main__':
    generator = TruthTableGenerator()
    count = generator.generate()
    print(count)