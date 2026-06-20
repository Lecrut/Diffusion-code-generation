class TruthValueManipulator:
    def get_opposite(self, value):
        return not value

if __name__ == '__main__':
    manipulator = TruthValueManipulator()
    test_value1 = False
    test_value2 = True
    print(f"Opposite of {test_value1}: {manipulator.get_opposite(test_value1)}")
    print(f"Opposite of {test_value2}: {manipulator.get_opposite(test_value2)}")