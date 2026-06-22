class TruthValueManipulator:
    FALSE_VAL = False
    TRUE_VAL = True

    def get_opposite(self, value):
        if value is self.TRUE_VAL:
            return self.FALSE_VAL
        if value is self.FALSE_VAL:
            return self.TRUE_VAL
        raise ValueError("Input must be a boolean")

if __name__ == '__main__':
    manipulator = TruthValueManipulator()
    first_input = True
    first_output = manipulator.get_opposite(first_input)
    print(first_output)
    second_input = False
    second_output = manipulator.get_opposite(second_input)
    print(second_output)