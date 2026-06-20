class LogicGate:
    def nand(self, a: bool, b: bool) -> bool:
        return not (a and b)

if __name__ == '__main__':
    gate = LogicGate()
    result1 = gate.nand(True, False)
    print(f"gate.nand(True, False): {result1}")
    result2 = gate.nand(False, True)
    print(f"gate.nand(False, True): {result2}")
    result3 = gate.nand(True, True)
    print(f"gate.nand(True, True): {result3}")
    result4 = gate.nand(False, False)
    print(f"gate.nand(False, False): {result4}")