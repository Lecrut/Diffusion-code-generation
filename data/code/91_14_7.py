class BoolFlipper:
    def flip_bool_value(self, value: bool) -> bool:
        return not value

if __name__ == '__main__':
    flipper = BoolFlipper()
    print(flipper.flip_bool_value(True))
    print(flipper.flip_bool_value(False))