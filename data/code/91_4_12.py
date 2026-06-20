class BooleanNegator:
    @staticmethod
    def negate(boolean: bool) -> bool:
        return not boolean

if __name__ == '__main__':
    sample1 = True
    result1 = BooleanNegator.negate(sample1)
    print(f"Input: {sample1}, Output: {result1}")
    sample2 = False
    result2 = BooleanNegator.negate(sample2)
    print(f"Input: {sample2}, Output: {result2}")