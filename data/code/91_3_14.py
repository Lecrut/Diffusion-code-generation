class BooleanFlipper:
    def flip(self, value: bool) -> bool:
        return not value

if __name__ == '__main__':
    flipper = BooleanFlipper()
    print(flipper.flip(True))
    print(flipper.flip(False))