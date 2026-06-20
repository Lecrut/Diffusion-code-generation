class LogicGates:

    def and_gate(self, a: int, b: int) -> int:
        if not (isinstance(a, int) and isinstance(b, int)):
            raise TypeError('Inputs must be integers')
        return a & b

    def or_gate(self, a: int, b: int) -> int:
        if not (isinstance(a, int) and isinstance(b, int)):
            raise TypeError('Inputs must be integers')
        return a | b

    def not_gate(self, a: int) -> int:
        if not isinstance(a, int):
            raise TypeError('Input must be an integer')
        return ~a

    def xor_gate(self, a: int, b: int) -> int:
        if not (isinstance(a, int) and isinstance(b, int)):
            raise TypeError('Inputs must be integers')
        return a ^ b
if __name__ == '__main__':
    lg = LogicGates()
    print(lg.and_gate(1, 0))
    print(lg.or_gate(1, 0))
    print(lg.not_gate(1))
    print(lg.xor_gate(1, 0))