class TruthValueManipulator:
    def get_opposite(self, value):
        return not value

if __name__ == '__main__':
    manipulator = TruthValueManipulator()
    sample_value1 = True
    sample_value2 = False
    print(f"Opposite of {sample_value1}: {manipulator.get_opposite(sample_value1)}")
    print(f"Opposite of {sample_value2}: {manipulator.get_opposite(sample_value2)}")