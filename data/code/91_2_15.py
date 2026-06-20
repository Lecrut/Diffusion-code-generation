class BooleanManipulator:
    @staticmethod
    def negate(value: bool) -> bool:
        return not value

if __name__ == '__main__':
    instance = BooleanManipulator()
    sample1 = True
    sample2 = False
    print(f"Negation of {sample1}: {instance.negate(sample1)}")
    print(f"Negation of {sample2}: {instance.negate(sample2)}")