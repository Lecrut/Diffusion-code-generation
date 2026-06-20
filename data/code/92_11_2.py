class TruthValueManipulator:
    def get_opposite(self, value):
        if value:
            return False
        else:
            return True

if __name__ == '__main__':
    manipulator = TruthValueManipulator()
    print(f"Opposite of True: {manipulator.get_opposite(True)}")
    print(f"Opposite of False: {manipulator.get_opposite(False)}")