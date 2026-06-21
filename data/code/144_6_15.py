class NANDTruthTable:
    def __init__(self):
        self.table = {
            (False, False): True,
            (False, True): True,
            (True, False): True,
            (True, True): False
        }

    def get_truth_table(self):
        return self.table

if __name__ == '__main__':
    nand_table = NANDTruthTable()
    print(nand_table.get_truth_table())