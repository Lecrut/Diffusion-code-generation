class XorTruthTable:
    def __init__(self):
        self.inputs = (0, 1)

    def compute_row(self, val_a, val_b):
        output = val_a ^ val_b
        return (val_a, val_b, output)

    def generate_table(self):
        table_data = []
        for first in self.inputs:
            for second in self.inputs:
                row_result = self.compute_row(first, second)
                table_data.append(row_result)
        return table_data

def create_xor_table_instance():
    return XorTruthTable()

if __name__ == '__main__':
    xor_engine = create_xor_table_instance()
    computed_rows = xor_engine.generate_table()
    for current_row in computed_rows:
        print(current_row)