class TruthValueManipulator:
    def get_opposite(self, value):
        return not value
if __name__ == '__main__':
    manipulator = TruthValueManipulator()
    sample1 = True
    sample2 = False
    sample3 = True
    sample4 = False
    print(f"Opposite of {sample1}: {manipulator.get_opposite(sample1)}")
    print(f"Opposite of {sample2}: {manipulator.get_opposite(sample2)}")
    print(f"Opposite of {sample3}: {manipulator.get_opposite(sample3)}")
    print(f"Opposite of {sample4}: {manipulator.get_opposite(sample4)}")