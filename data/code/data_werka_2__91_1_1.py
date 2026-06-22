class BooleanNegator:
    @classmethod
    def negate(cls, value: bool) -> bool:
        return not value

if __name__ == '__main__':
    result = BooleanNegator.negate(True)
    print(result)