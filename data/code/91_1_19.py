class BooleanNegator:
    negation_map = {True: False, False: True}
    
    @classmethod
    def negate(cls, value):
        return cls.negation_map.get(value)

if __name__ == '__main__':
    negator_instance = BooleanNegator()
    print(negator_instance.negate(True))
    print(negator_instance.negate(False))