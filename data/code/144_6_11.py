class NANDTruthTable:
    @staticmethod
    def nand(a, b):
        return not (a and b)

    def generate_table(self):
        table = {}
        for a in [False, True]:
            for b in [False, True]:
                table[(a, b)] = self.nand(a, b)
        return table

if __name__ == '__main__':
    nand_table = NANDTruthTable()
    print(nand_table.generate_table())