class TruthTableGenerator:
    def __init__(self):
        self.variables = ['A', 'B', 'C']

    def generate(self):
        table = []
        for i in range(8):
            a = (i >> 2) & 1
            b = (i >> 1) & 1
            c = i & 1
            row = {
                'A': a,
                'B': b,
                'C': c,
                'NOT_A': not a,
                'NOT_B': not b,
                'NOT_C': not c,
                'A_AND_B': a and b,
                'A_OR_B': a or b,
                'A_XOR_B': a ^ b,
                'A_IMPLIES_B': (not a) or b,
                'A_NAND_B': not (a and b),
                'A_XNOR_B': not (a ^ b),
                'A_AND_B_AND_C': a and b and c,
                'A_OR_B_OR_C': a or b or c,
                'A_XOR_B_XOR_C': a ^ b ^ c
            }
            table.append(row)
        return table

    def display(self, table):
        header = f"{'A':<5} {'B':<5} {'C':<5} | {'NOT A':<7} {'NOT B':<7} {'NOT C':<7} | {'A&B':<5} {'A|B':<5} {'A^B':<5} | {'A->B':<6} {'A|B':<5} {'A~B':<5} | {'A&B&C':<7} {'A|B|C':<7} {'A^B^C':<7}"
        print(header)
        print("-" * len(header))
        for row in table:
            line = f"{int(row['A']):<5} {int(row['B']):<5} {int(row['C']):<5} | {int(row['NOT_A']):<7} {int(row['NOT_B']):<7} {int(row['NOT_C']):<7} | {int(row['A_AND_B']):<5} {int(row['A_OR_B']):<5} {int(row['A_XOR_B']):<5} | {int(row['A_IMPLIES_B']):<6} {int(row['A_NAND_B']):<5} {int(row['A_XNOR_B']):<5} | {int(row['A_AND_B_AND_C']):<7} {int(row['A_OR_B_OR_C']):<7} {int(row['A_XOR_B_XOR_C']):<7}"
            print(line)

if __name__ == '__main__':
    generator = TruthTableGenerator()
    table = generator.generate()
    generator.display(table)
    print(table[0])