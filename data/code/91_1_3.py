class BooleanLogic:
    @classmethod
    def negate(cls, value: bool) -> bool:
        return not value

if __name__ == '__main__':
    print(BooleanLogic.negate(True))
    print(BooleanLogic.negate(False))