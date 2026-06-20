class BooleanNegator:

    @classmethod
    def negate(cls, value: bool) -> bool:
        return not value
if __name__ == '__main__':
    negator_instance = BooleanNegator()
    sample_value1 = True
    sample_value2 = False
    result1 = negator_instance.negate(sample_value1)
    result2 = negator_instance.negate(sample_value2)
    print(result1)
    print(result2)