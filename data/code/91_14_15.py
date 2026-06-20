class BoolInverter:
    def flip_bool_value(self, value: bool) -> bool:
        return not value

if __name__ == '__main__':
    inverter = BoolInverter()
    print(inverter.flip_bool_value(True))
    print(inverter.flip_bool_value(False))