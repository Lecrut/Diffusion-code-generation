class TruthValueManipulator:
    def is_valid_input(self, value):
        return isinstance(value, bool)

    def get_opposite(self, value):
        if not self.is_valid_input(value):
            raise ValueError("Input must be a boolean")
        return not value

if __name__ == '__main__':
    manipulator = TruthValueManipulator()
    print(f"Opposite of True: {manipulator.get_opposite(True)}")
    print(f"Opposite of False: {manipulator.get_opposite(False)}")