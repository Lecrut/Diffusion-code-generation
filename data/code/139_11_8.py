class LogicGate:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def and_gate(self):
        return self.a and self.b

    def or_gate(self):
        return self.a or self.b

    def not_a(self):
        return not self.a

if __name__ == '__main__':
    gate1 = LogicGate(True, False)
    print(f"AND (True, False): {gate1.and_gate()}")
    print(f"OR (True, False): {gate1.or_gate()}")
    print(f"NOT (of True): {gate1.not_a()}")

    gate2 = LogicGate(False, True)
    print(f"\nAND (False, True): {gate2.and_gate()}")
    print(f"OR (False, True): {gate2.or_gate()}")
    print(f"NOT (of False): {gate2.not_a()}")