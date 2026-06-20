class BooleanNegator:
    TRUE = True
    FALSE = False
    
    @classmethod
    def negate(cls, value):
        return not value

if __name__ == '__main__':
    negator = BooleanNegator()
    print(negator.negate(BooleanNegator.TRUE))
    print(negator.negate(BooleanNegator.FALSE))