class LogicGate:
    def nand(self, a: bool, b: bool) -> bool:
        return not (a and b)

if __name__ == '__main__':
    gate = LogicGate()
    result1 = gate.nand(True, False)
    print(f"nand(True, False): {result1}")
    result2 = gate.nand(False, True)
    print(f"nand(False, True): {result2}")