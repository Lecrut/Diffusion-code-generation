class BooleanLogic:

    def custom_and(self, a, b):
        return 1 if a == 1 and b == 1 else 0

    def custom_or(self, a, b):
        return 1 if a == 1 or b == 1 else 0

    def custom_not(self, a):
        return 1 - a
if __name__ == '__main__':
    logic = BooleanLogic()
    print(logic.custom_and(1, 1))
    print(logic.custom_and(0, 1))
    print(logic.custom_and(1, 0))
    print(logic.custom_and(0, 0))
    print(logic.custom_or(1, 1))
    print(logic.custom_or(0, 1))
    print(logic.custom_or(1, 0))
    print(logic.custom_or(0, 0))
    print(logic.custom_not(1))
    print(logic.custom_not(0))