class BooleanComparator:
    @staticmethod
    def check_boolean_equality(value1: bool, value2: bool) -> bool:
        return value1 == value2

if __name__ == '__main__':
    sample_a = True
    sample_b = False
    result = BooleanComparator.check_boolean_equality(sample_a, sample_b)
    print(f"Input A: {sample_a}, Input B: {sample_b}, Equality Result: {result}")