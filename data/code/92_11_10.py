class TruthValueManipulator:
    def get_opposite(self, value):
        return not value

if __name__ == '__main__':
    truth_manipulator = TruthValueManipulator()
    print(f"Opposite of True: {truth_manipulator.get_opposite(True)}")
    print(f"Opposite of False: {truth_manipulator.get_opposite(False)}")