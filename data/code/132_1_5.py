class LogicGate:
    def nand(self, a: bool, b: bool) -> bool:
        if not isinstance(a, bool) or not isinstance(b, bool):
            raise ValueError("Inputs must be boolean values")
        return not (a and b)

if __name__ == '__main__':
    gate = LogicGate()
    print(gate.nand(True, False))