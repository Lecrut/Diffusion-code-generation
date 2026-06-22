class TruthValueManipulator:
    _OPPOSITE_MAP = {True: False, False: True}

    def get_opposite(self, value):
        if not isinstance(value, bool):
            raise ValueError("Input must be a boolean")
        return self._OPPOSITE_MAP[value]

if __name__ == '__main__':
    manipulator = TruthValueManipulator()
    result_true = manipulator.get_opposite(True)
    result_false = manipulator.get_opposite(False)
    print(result_true)
    print(result_false)