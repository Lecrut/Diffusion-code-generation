class BooleanLogic:
    TRUE = 1
    FALSE = 0

    @staticmethod
    def custom_and(a, b):
        return BooleanLogic.TRUE if a == BooleanLogic.TRUE and b == BooleanLogic.TRUE else BooleanLogic.FALSE

    @staticmethod
    def custom_or(a, b):
        return BooleanLogic.TRUE if a == BooleanLogic.TRUE or b == BooleanLogic.TRUE else BooleanLogic.FALSE

    @staticmethod
    def custom_not(a):
        return BooleanLogic.TRUE if a == BooleanLogic.FALSE else BooleanLogic.FALSE
if __name__ == '__main__':
    logic = BooleanLogic()
    a_val = BooleanLogic.TRUE
    b_val = BooleanLogic.FALSE
    c_val = BooleanLogic.TRUE
    print(logic.custom_and(a_val, b_val))
    print(logic.custom_or(a_val, b_val))
    print(logic.custom_not(c_val))