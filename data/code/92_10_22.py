class TruthValueManipulator:
    def __init__(self):
        self._truth_table = {True: False, False: True}

    def get_opposite(self, value):
        if value not in (True, False):
            raise ValueError("Input must be a boolean")
        return self._truth_table[value]

if __name__ == '__main__':
    manipulator = TruthValueManipulator()
    print(manipulator.get_opposite(True))
    print(manipulator.get_opposite(False))
    print(manipulator.get_opposite(not True))
    print(manipulator.get_opposite(not False))