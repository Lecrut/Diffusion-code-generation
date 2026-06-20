class BooleanNegator:
    @classmethod
    def negate(cls, value: bool) -> bool:
        return not value

if __name__ == '__main__':
    negator_instance = BooleanNegator()
    result1 = negator_instance.negate(True)
    result2 = negator_instance.negate(False)
    
    print(result1)
    print(result2)