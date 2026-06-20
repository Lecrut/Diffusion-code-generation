class LogicGate:
    def nand(self, a, b):
        return not (a and b)

if __name__ == '__main__':
    gate = LogicGate()
    output1 = gate.nand(True, False)
    print(f"LogicGate().nand(True, False): {output1}")
    output2 = gate.nand(False, True)
    print(f"LogicGate().nand(False, True): {output2}")