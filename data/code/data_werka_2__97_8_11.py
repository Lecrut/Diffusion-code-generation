class BooleanLogic:
    def __init__(self, val_a, val_b):
        self.a = val_a
        self.b = val_b

    def get_table(self):
        return {
            "inputs": (self.a, self.b),
            "a_and_b": self.a and self.b,
            "a_or_b": self.a or self.b,
            "a_xor_b": self.a ^ self.b,
            "a_nand_b": not (self.a and self.b),
            "a_nor_b": not (self.a or self.b),
            "a_implies_b": (not self.a) or self.b,
            "b_implies_a": (not self.b) or self.a,
            "a_eq_b": self.a == self.b,
            "a_neq_b": self.a != self.b
        }

if __name__ == '__main__':
    logic = BooleanLogic(True, False)
    result = logic.get_table()
    print(result)
    print(logic.a)
    print(logic.b)