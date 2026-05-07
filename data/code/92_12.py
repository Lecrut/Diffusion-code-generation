class TruthValueManipulator:
    def get_opposite(self, value):
        return not value
if __name__ == '__main__':
    manipulator = TruthValueManipulator()
    sample1 = True
    opposite1 = manipulator.get_opposite(sample1)
    print(f"Original: {sample1}, Opposite: {opposite1}")
    sample2 = False
    opposite2 = manipulator.get_opposite(sample2)
    print(f"Original: {sample2}, Opposite: {opposite2}")