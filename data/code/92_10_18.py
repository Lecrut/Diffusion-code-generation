class TruthValueManipulator:
    def __init__(self):
        self._table = {True: False, False: True}

    def get_opposite(self, value):
        try:
            return self._table[value]
        except KeyError:
            raise ValueError("Input must be a boolean")

if __name__ == '__main__':
    manipulator = TruthValueManipulator()
    print(manipulator.get_opposite(True))
    print(manipulator.get_opposite(False))
    print(manipulator.get_opposite(1 == 1))
    print(manipulator.get_opposite(0 == 0))