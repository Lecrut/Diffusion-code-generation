class TruthValueManipulator:
    OPPOSITE_MAP = {True: False, False: True}

    def get_opposite(self, value):
        if value not in self.OPPOSITE_MAP:
            raise ValueError("Input must be a boolean")
        return self.OPPOSITE_MAP[value]

if __name__ == '__main__':
    manipulator = TruthValueManipulator()
    print(manipulator.get_opposite(True))
    print(manipulator.get_opposite(False))