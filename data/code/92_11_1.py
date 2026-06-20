class TruthValueManipulator:

    def get_opposite(self, value):
        return not value
if __name__ == '__main__':
    manipulator = TruthValueManipulator()
    print(manipulator.get_opposite(True))
    print(manipulator.get_opposite(False))