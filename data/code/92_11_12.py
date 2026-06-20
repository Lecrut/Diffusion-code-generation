class TruthValueManipulator:
    TRUTH_MAP = {True: False, False: True}

    def get_opposite(self, value):
        return self.TRUTH_MAP.get(value, None)

if __name__ == '__main__':
    manipulator = TruthValueManipulator()
    print(f"Opposite of True: {manipulator.get_opposite(True)}")
    print(f"Opposite of False: {manipulator.get_opposite(False)}")