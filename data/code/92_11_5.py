class TruthValueManipulator:
    OPPOSITE_MAP = {True: False, False: True}

    def get_opposite(self, value):
        return self.OPPOSITE_MAP[value]

if __name__ == '__main__':
    manipulator = TruthValueManipulator()
    print(f"Opposite of True: {manipulator.get_opposite(True)}")
    print(f"Opposite of False: {manipulator.get_opposite(False)}")