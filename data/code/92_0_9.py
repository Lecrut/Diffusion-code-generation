class BooleanFlipper:
    def __init__(self, flag: bool):
        if not isinstance(flag, bool):
            raise ValueError("Input must be a boolean")
        self.flag = flag

    def flip(self) -> bool:
        return not self.flag

if __name__ == '__main__':
    flipper_true = BooleanFlipper(True)
    print(flipper_true.flip())
    
    flipper_false = BooleanFlipper(False)
    print(flipper_false.flip())