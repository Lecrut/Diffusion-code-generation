class BooleanInverter:
    def __init__(self):
        self.bool_map = {'True': 'False', 'False': 'True'}

    def get_opposite_boolean_string(self, bool_str):
        return self.bool_map.get(bool_str, None)

if __name__ == '__main__':
    inverter = BooleanInverter()
    print(inverter.get_opposite_boolean_string('True'))
    print(inverter.get_opposite_boolean_string('False'))
    print(inverter.get_opposite_boolean_string('SomethingElse'))