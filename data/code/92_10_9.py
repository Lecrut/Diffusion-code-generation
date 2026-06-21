class TruthValueManipulator:
    def get_opposite(self, value):
        if not isinstance(value, bool):
            raise ValueError("Input must be a boolean")
        return True if value is False else False

if __name__ == '__main__':
    manipulator = TruthValueManipulator()
    sample_input_1 = True
    sample_input_2 = False
    result_1 = manipulator.get_opposite(sample_input_1)
    result_2 = manipulator.get_opposite(sample_input_2)
    print(result_1)
    print(result_2)