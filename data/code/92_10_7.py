class TruthValueManipulator:
    _MAPPING = {True: False, False: True}

    @staticmethod
    def _validate(value):
        if not isinstance(value, bool):
            raise ValueError("Input must be a boolean")

    def get_opposite(self, value):
        self._validate(value)
        return self._MAPPING[value]

if __name__ == '__main__':
    manipulator = TruthValueManipulator()
    print(manipulator.get_opposite(True))
    print(manipulator.get_opposite(False))