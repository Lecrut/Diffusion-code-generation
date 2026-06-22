class TruthValueManipulator:
    _TRUE_VALUE = True
    _FALSE_VALUE = False

    @staticmethod
    def _validate_boolean(value):
        if value is not TruthValueManipulator._TRUE_VALUE and value is not TruthValueManipulator._FALSE_VALUE:
            raise ValueError("Input must be a boolean")
        return True

    def get_opposite(self, value):
        self._validate_boolean(value)
        if value is self._TRUE_VALUE:
            return self._FALSE_VALUE
        return self._TRUE_VALUE

if __name__ == '__main__':
    manipulator = TruthValueManipulator()
    print(manipulator.get_opposite(True))
    print(manipulator.get_opposite(False))