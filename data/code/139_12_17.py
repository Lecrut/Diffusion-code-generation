class LogicGates:
    @staticmethod
    def AND(a, b):
        return a & b

    @staticmethod
    def OR(a, b):
        return a | b

    @staticmethod
    def NOT(a):
        return 1 - a

    @staticmethod
    def NAND(a, b):
        return LogicGates.NOT(LogicGates.AND(a, b))

    @staticmethod
    def NOR(a, b):
        return LogicGates.NOT(LogicGates.OR(a, b))

    @staticmethod
    def XOR(a, b):
        return a ^ b

    @staticmethod
    def XNOR(a, b):
        return 1 - (a ^ b)

if __name__ == '__main__':
    input_a = 1
    input_b = 0
    print(f"Input A: {input_a}")
    print(f"Input B: {input_b}")
    and_out = LogicGates.AND(input_a, input_b)
    or_out = LogicGates.OR(input_a, input_b)
    not_a = LogicGates.NOT(input_a)
    not_b = LogicGates.NOT(input_b)
    nand_out = LogicGates.NAND(input_a, input_b)
    nor_out = LogicGates.NOR(input_a, input_b)
    xor_out = LogicGates.XOR(input_a, input_b)
    xnor_out = LogicGates.XNOR(input_a, input_b)
    print("--- Results ---")
    print(f"AND ({input_a} AND {input_b}): {and_out}")
    print(f"OR ({input_a} OR {input_b}): {or_out}")
    print(f"NOT A (NOT {input_a}): {not_a}")
    print(f"NOT B (NOT {input_b}): {not_b}")
    print(f"NAND ({input_a} NAND {input_b}): {nand_out}")
    print(f"NOR ({input_a} NOR {input_b}): {nor_out}")
    print(f"XOR ({input_a} XOR {input_b}): {xor_out}")
    print(f"XNOR ({input_a} XNOR {input_b}): {xnor_out}")