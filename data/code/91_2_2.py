class BooleanManipulator:
    @staticmethod
    def negate_boolean(value: bool) -> bool:
        return not value
if __name__ == '__main__':
    sample1 = True
    result1 = BooleanManipulator.negate_boolean(sample1)
    print(f"Negation of {sample1}: {result1}")
    sample2 = False
    result2 = BooleanManipulator.negate_boolean(sample2)
    print(f"Negation of {sample2}: {result2}")