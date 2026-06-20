class TruthValueManipulator:
    def get_opposite(self, value):
        return not value

if __name__ == '__main__':
    manipulator = TruthValueManipulator()
    sample_values = [True, False]
    for val in sample_values:
        print(f"Opposite of {val}: {manipulator.get_opposite(val)}")