class NANDGate:
    INPUTS = [(True, True), (True, False), (False, True), (False, False)]
    
    @staticmethod
    def nand_gate(a, b):
        return not (a and b)
    
    @classmethod
    def generate_truth_table(cls):
        results = {input: cls.nand_gate(*input) for input in cls.INPUTS}
        return results

if __name__ == '__main__':
    truth_table = NANDGate.generate_truth_table()
    print(truth_table)