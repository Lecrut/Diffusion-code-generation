class NANDTruthTableGenerator:
    NAND_TABLE = {
        (False, False): True,
        (False, True): True,
        (True, False): True,
        (True, True): False
    }

    @staticmethod
    def generate_truth_table():
        return NAND_TABLE

if __name__ == '__main__':
    generator = NANDTruthTableGenerator()
    print(generator.generate_truth_table())