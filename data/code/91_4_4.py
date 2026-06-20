class BooleanNegator:
    def negate(self, value: bool) -> bool:
        return not value

if __name__ == '__main__':
    negator = BooleanNegator()
    sample1 = True
    result1 = negator.negate(sample1)
    print(f"Input: {sample1}, Output: {result1}")
    sample2 = False
    result2 = negator.negate(sample2)
    print(f"Input: {sample2}, Output: {result2}")