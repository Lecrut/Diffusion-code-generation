class BooleanLogic:
    def __init__(self, val_a, val_b):
        self.a = val_a
        self.b = val_b

    def get_table(self):
        return {
            "a": self.a,
            "b": self.b,
            "a and b": self.a and self.b,
            "a or b": self.a or self.b,
            "a xor b": self.a ^ self.b,
            "not a": not self.a,
            "not b": not self.b,
            "a implies b": (not self.a) or self.b,
            "b implies a": (not self.b) or self.a,
            "a nand b": not (self.a and self.b),
            "a nor b": not (self.a or self.b),
            "a eq b": self.a == self.b
        }

if __name__ == '__main__':
    logic = BooleanLogic(True, False)
    print(logic.get_table())
    logic2 = BooleanLogic(False, True)
    print(logic2.get_table())