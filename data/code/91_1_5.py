class BooleanNegator:
    @classmethod
    def negate(cls, value: bool) -> bool:
        return not value

if __name__ == '__main__':
    negator = BooleanNegator()
    sample1 = True
    sample2 = False
    result1 = negator.negate(sample1)
    result2 = negator.negate(sample2)
    print(result1)
    print(result2)