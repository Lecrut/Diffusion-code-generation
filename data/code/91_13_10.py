class BooleanNegator:
    TRUE = True
    FALSE = False
    
    @staticmethod
    def negate_boolean(b):
        return bool(~int(b))

if __name__ == '__main__':
    negator = BooleanNegator()
    print(negator.negate_boolean(True))
    print(negator.negate_boolean(False))