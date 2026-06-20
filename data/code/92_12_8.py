class TruthValueManipulator:
    TRUE = 'True'
    FALSE = 'False'

    @staticmethod
    def is_true(value):
        return value.lower() == TruthValueManipulator.TRUE

    @staticmethod
    def get_opposite(value):
        if TruthValueManipulator.is_true(value):
            return TruthValueManipulator.FALSE
        elif value.lower() == TruthValueManipulator.FALSE:
            return TruthValueManipulator.TRUE
        else:
            raise ValueError("Invalid boolean string")

if __name__ == '__main__':
    manipulator = TruthValueManipulator()
    sample1 = 'True'
    opposite1 = manipulator.get_opposite(sample1)
    print(f"Original: {sample1}, Opposite: {opposite1}")
    sample2 = 'False'
    opposite2 = manipulator.get_opposite(sample2)
    print(f"Original: {sample2}, Opposite: {opposite2}")