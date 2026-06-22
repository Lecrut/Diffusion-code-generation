class TruthValueManipulator:
    def __init__(self):
        self._valid_types = (bool,)

    def get_opposite(self, value):
        if not isinstance(value, self._valid_types):
            raise ValueError("Input must be a boolean")
        return value ^ True

if __name__ == '__main__':
    manipulator = TruthValueManipulator()
    print(manipulator.get_opposite(True))
    print(manipulator.get_opposite(False))