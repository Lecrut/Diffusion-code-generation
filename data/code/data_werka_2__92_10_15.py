class TruthValueManipulator:
    _OPPOSITE_MAP = {True: False, False: True}

    @staticmethod
    def _validate_input(value):
        if not isinstance(value, bool):
            raise ValueError("Input must be a boolean")

    def get_opposite(self, value):
        self._validate_input(value)
        return self._OPPOSITE_MAP[value]

if __name__ == '__main__':
    manipulator = TruthValueManipulator()
    print(manipulator.get_opposite(True))
    print(manipulator.get_opposite(False))