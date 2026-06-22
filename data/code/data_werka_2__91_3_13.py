class BooleanFlipper:
    TRUE_BIT: int = 1
    FALSE_BIT: int = 0

    @staticmethod
    def flip(value: bool) -> bool:
        return bool(int(value) ^ BooleanFlipper.TRUE_BIT)

if __name__ == '__main__':
    print(BooleanFlipper.flip(True))
    print(BooleanFlipper.flip(False))