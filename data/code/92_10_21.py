class TruthValueManipulator:
    _VALID_TRUE = True
    _VALID_FALSE = False

    def get_opposite(self, value):
        if value is self._VALID_TRUE:
            return self._VALID_FALSE
        if value is self._VALID_FALSE:
            return self._VALID_TRUE
        raise ValueError("Input must be a boolean")

if __name__ == '__main__':
    manipulator = TruthValueManipulator()
    print(manipulator.get_opposite(True))
    print(manipulator.get_opposite(False))