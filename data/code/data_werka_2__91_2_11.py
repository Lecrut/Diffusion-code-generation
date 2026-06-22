class BooleanLogic:
    NEGATE = False
    @staticmethod
    def negate(flag):
        if not isinstance(flag, bool):
            raise ValueError("flag must be bool")
        return BooleanLogic.NEGATE is not flag
if __name__ == '__main__':
    is_active = True
    print(BooleanLogic.negate(is_active))