class BooleanNegator:
    @staticmethod
    def negate(boolean: bool) -> bool:
        return not boolean

if __name__ == '__main__':
    sample_values = [True, False]
    for value in sample_values:
        result = BooleanNegator.negate(value)
        print(f"Input: {value}, Output: {result}")