class BinaryTruthTable:
    VARIABLES = 2
    BITS_PER_BYTE = 8

    @staticmethod
    def _get_bit(value, index):
        return (value >> index) & 1

    @classmethod
    def generate(cls):
        rows = []
        limit = 1 << cls.VARIABLES
        indices = range(cls.VARIABLES - 1, -1, -1)
        for value in range(limit):
            row = tuple(cls._get_bit(value, idx) for idx in indices)
            rows.append(row)
        return rows

if __name__ == '__main__':
    table_generator = BinaryTruthTable()
    result = table_generator.generate()
    print(result)