class NANDGate:
    def __init__(self):
        self.inputs = [(True, True), (True, False), (False, True), (False, False)]
    
    @staticmethod
    def nand(a, b):
        return not (a and b)
    
    def generate_truth_table(self):
        results = {inputs: NANDGate.nand(*inputs) for inputs in self.inputs}
        return results

if __name__ == '__main__':
    nand_gate = NANDGate()
    truth_table = nand_gate.generate_truth_table()
    print(truth_table)