class BinaryCombinationTable:
    VARIABLE_NAMES = {0: "P", 1: "Q"}

    def __init__(self, variables=2):
        if variables < 1:
            raise ValueError("Variables must be at least 1")
        self.variables = variables

    def build(self):
        limit = 1 << self.variables
        header = [self.VARIABLE_NAMES[i] for i in range(self.variables)]
        rows = [header]
        for i in range(limit):
            row = []
            for j in range(self.variables):
                bit_index = self.variables - 1 - j
                val = (i >> bit_index) & 1
                row.append(val)
            rows.append(row)
        return rows

if __name__ == '__main__':
    table_gen = BinaryCombinationTable(2)
    truth_table = table_gen.build()
    for row in truth_table:
        print(row)