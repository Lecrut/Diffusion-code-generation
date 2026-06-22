class BinaryVariableCombiner:
    NUM_VARS = 2
    MASK = 0

    def __init__(self, num_vars=2):
        if not isinstance(num_vars, int) or num_vars <= 0:
            raise ValueError("num_vars must be a positive integer")
        self.num_vars = num_vars
        self.MASK = (1 << num_vars) - 1

    def compute_combinations(self):
        rows = []
        for counter in range(1 << self.num_vars):
            row = [0] * self.num_vars
            temp = counter
            for idx in range(self.num_vars - 1, -1, -1):
                row[idx] = temp & 1
                temp >>= 1
            rows.append(tuple(row))
        return rows

if __name__ == '__main__':
    combiner = BinaryVariableCombiner(2)
    output = combiner.compute_combinations()
    print(output)