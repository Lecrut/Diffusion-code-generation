class BinaryTruthTable:
    VAR_COUNT = 2
    BITS = [0, 1]

    def __init__(self, variables=2):
        if variables < 1:
            raise ValueError("variables must be positive")
        self.variables = variables

    @staticmethod
    def _extract_bits(value, count):
        bits = []
        for i in range(count - 1, -1, -1):
            bits.append((value >> i) & 1)
        return bits

    def generate(self):
        total = 1 << self.variables
        table = []
        for i in range(total):
            row = self._extract_bits(i, self.variables)
            table.append(row)
        return table

if __name__ == '__main__':
    table_gen = BinaryTruthTable(2)
    result = table_gen.generate()
    print(result)