class NANDTruthTable:
    def __init__(self):
        self.table = {
            (True, True): False,
            (True, False): True,
            (False, True): True,
            (False, False): True
        }

    def get_result(self, a, b):
        return self.table[(a, b)]

if __name__ == '__main__':
    nand_table = NANDTruthTable()
    print(nand_table.get_result(True, True))
    print(nand_table.get_result(True, False))
    print(nand_table.get_result(False, True))
    print(nand_table.get_result(False, False))