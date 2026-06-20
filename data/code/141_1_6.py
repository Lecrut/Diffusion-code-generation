class CustomLogic:

    def and_gate(self, a, b):
        return 1 if a == 1 and b == 1 else 0

    def or_gate(self, a, b):
        return 1 if a == 1 or b == 1 else 0

    def not_gate(self, a):
        return 1 - a
if __name__ == '__main__':
    logic = CustomLogic()
    print(logic.and_gate(1, 1))
    print(logic.or_gate(0, 1))
    print(logic.not_gate(0))