class BooleanNegator:
    @classmethod
    def negate(cls, value: bool) -> bool:
        return not value

if __name__ == '__main__':
    negator = BooleanNegator()
    result1 = negator.negate(True)
    result2 = negator.negate(False)
    print(result1)
    print(result2)