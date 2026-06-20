class BooleanInverter:
    TRUE = 'True'
    FALSE = 'False'

    @staticmethod
    def get_opposite_boolean_string(bool_str):
        if bool_str == BooleanInverter.TRUE:
            return BooleanInverter.FALSE
        elif bool_str == BooleanInverter.FALSE:
            return BooleanInverter.TRUE
        else:
            return None

if __name__ == '__main__':
    print(BooleanInverter.get_opposite_boolean_string('True'))
    print(BooleanInverter.get_opposite_boolean_string('False'))
    print(BooleanInverter.get_opposite_boolean_string('SomethingElse'))