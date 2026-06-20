class BooleanNegator:
    def negate(self, value: bool) -> bool:
        return not value

if __name__ == '__main__':
    negator = BooleanNegator()
    sample1 = True
    print(f"Negation of {sample1}: {negator.negate(sample1)}")
    sample2 = False
    print(f"Negation of {sample2}: {negator.negate(sample2)}")