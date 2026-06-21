class BooleanFlipper:
    TRUE_VALUE: bool = True
    FALSE_VALUE: bool = False

    @staticmethod
    def invert(value: bool) -> bool:
        if value is BooleanFlipper.TRUE_VALUE:
            return BooleanFlipper.FALSE_VALUE
        return BooleanFlipper.TRUE_VALUE

def flip_bool_value(value: bool) -> bool:
    return BooleanFlipper.invert(value)

if __name__ == '__main__':
    print(flip_bool_value(True))
    print(flip_bool_value(False))