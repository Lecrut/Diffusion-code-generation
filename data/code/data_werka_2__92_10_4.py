class TruthValueManipulator:
    def get_opposite(self, value):
        if not isinstance(value, bool):
            raise ValueError("Input must be a boolean")
        return not value

if __name__ == '__main__':
    manipulator = TruthValueManipulator()
    print(manipulator.get_opposite(True))
    print(manipulator.get_opposite(False))