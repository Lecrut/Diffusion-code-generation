class TruthValueManipulator:
    _OPPOSITES = {True: False, False: True}

    def get_opposite(self, value):
        if value in self._OPPOSITES:
            return self._OPPOSITES[value]
        raise ValueError("Input must be a boolean")

if __name__ == '__main__':
    manipulator = TruthValueManipulator()
    print(manipulator.get_opposite(True))
    print(manipulator.get_opposite(False))