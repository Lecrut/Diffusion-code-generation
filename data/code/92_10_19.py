class TruthValueManipulator:
    _VALID_TRUE = True
    _VALID_FALSE = False

    def _validate_boolean(self, value):
        if value is self._VALID_TRUE:
            return True
        if value is self._VALID_FALSE:
            return False
        raise ValueError("Input must be a boolean type")

    def get_opposite(self, value):
        is_valid = self._validate_boolean(value)
        if is_valid:
            return self._VALID_FALSE
        return self._VALID_TRUE

if __name__ == '__main__':
    manipulator = TruthValueManipulator()
    result_true = manipulator.get_opposite(True)
    print(result_true)
    result_false = manipulator.get_opposite(False)
    print(result_false)