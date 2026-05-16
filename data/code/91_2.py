class BooleanManipulator:
    @staticmethod
    def negate(value: bool) -> bool:
        return not value
if __name__ == '__main__':
    print(BooleanManipulator.negate(True))
    print(BooleanManipulator.negate(False))