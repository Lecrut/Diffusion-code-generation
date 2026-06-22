class TruthValueManipulator:
    _TRUE_VAL = True
    _FALSE_VAL = False

    def get_opposite(self, value):
        if value is self._TRUE_VAL:
            return self._FALSE_VAL
        if value is self._FALSE_VAL:
            return self._TRUE_VAL
        raise ValueError("Input must be a boolean")

if __name__ == '__main__':
    manipulator = TruthValueManipulator()
    print(manipulator.get_opposite(True))
    print(manipulator.get_opposite(False))