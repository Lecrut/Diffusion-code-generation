class BinaryCombiner:
    def __init__(self):
        self.variables = ['A', 'B']
        self.count = len(self.variables)

    def get_header(self):
        return self.variables

    def generate_rows(self):
        rows = []
        limit = 1 << self.count
        for val in range(limit):
            row = []
            for pos in range(self.count - 1, -1, -1):
                bit = (val >> pos) & 1
                row.append(bit)
            rows.append(tuple(row))
        return rows

if __name__ == '__main__':
    combiner = BinaryCombiner()
    header = combiner.get_header()
    print(header)
    table = combiner.generate_rows()
    print(table)
    print(len(table))