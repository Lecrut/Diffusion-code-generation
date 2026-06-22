class TruthValueManipulator:
    _TRUE_CONSTANT = True
    _FALSE_CONSTANT = False

    def get_opposite(self, value):
        if value is self._TRUE_CONSTANT:
            return self._FALSE_CONSTANT
        if value is self._FALSE_CONSTANT:
            return self._TRUE_CONSTANT
        raise ValueError("Expected boolean input")

if __name__ == '__main__':
    manipulator = TruthValueManipulator()
    initial_value = True
    result = manipulator.get_opposite(initial_value)
    print(result)
    other_value = False
    other_result = manipulator.get_opposite(other_value)
    print(other_result)