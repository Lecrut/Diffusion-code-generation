class LogicGates:
    xor = lambda self, a, b: a ^ b

if __name__ == '__main__':
    gate_instance = LogicGates()
    print(gate_instance.xor(1, 0))
    print(gate_instance.xor(10, 5))
    print(gate_instance.xor(11, 11))