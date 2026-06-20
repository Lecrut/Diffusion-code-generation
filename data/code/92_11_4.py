class TruthValueManipulator:
    TRUE = True
    FALSE = False

    @staticmethod
    def get_opposite(value):
        return not value

if __name__ == '__main__':
    manipulator = TruthValueManipulator()
    print(f"Opposite of {TruthValueManipulator.TRUE}: {manipulator.get_opposite(TruthValueManipulator.TRUE)}")
    print(f"Opposite of {TruthValueManipulator.FALSE}: {manipulator.get_opposite(TruthValueManipulator.FALSE)}")