class BooleanNegator:

    @classmethod
    def negate(cls, value: bool) -> bool:
        return not value
if __name__ == '__main__':
    negator_instance = BooleanNegator()
    sample_input1 = True
    sample_input2 = False
    result1 = negator_instance.negate(sample_input1)
    result2 = negator_instance.negate(sample_input2)
    print(result1)
    print(result2)