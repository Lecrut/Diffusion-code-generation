class BooleanNegator:
    @staticmethod
    def negate(value: bool) -> bool:
        return not value

if __name__ == '__main__':
    sample1 = True
    result1 = BooleanNegator.negate(sample1)
    print(f"Negated {sample1}: {result1}")
    sample2 = False
    result2 = BooleanNegator.negate(sample2)
    print(f"Negated {sample2}: {result2}")