class TruthValueManipulator:
    def get_opposite(self, value):
        if value is True:
            return False
        if value is False:
            return True
        raise ValueError("Input must be a boolean")

if __name__ == '__main__':
    manipulator = TruthValueManipulator()
    print(manipulator.get_opposite(True))
    print(manipulator.get_opposite(False))