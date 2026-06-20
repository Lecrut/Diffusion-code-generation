class BooleanInverter:
    TRUE = 'True'
    FALSE = 'False'

    @staticmethod
    def get_opposite(boolean_str):
        return BooleanInverter.FALSE if boolean_str == BooleanInverter.TRUE else BooleanInverter.TRUE

if __name__ == '__main__':
    print(BooleanInverter.get_opposite('True'))
    print(BooleanInverter.get_opposite('False'))
    print(BooleanInverter.get_opposite('True'))
    print(BooleanInverter.get_opposite('SomethingElse'))