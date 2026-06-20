class LogicGate:
    def __init__(self, gate_type):
        self.gate_type = gate_type

    @staticmethod
    def and_gate(a, b):
        return a and b

    @staticmethod
    def or_gate(a, b):
        return a or b

    @staticmethod
    def not_gate(a):
        return not a

if __name__ == '__main__':
    gate = LogicGate('and')
    print(f"AND: {LogicGate.and_gate(True, False)}")
    print(f"OR: {LogicGate.or_gate(True, False)}")
    print(f"NOT (of True): {LogicGate.not_gate(True)}")