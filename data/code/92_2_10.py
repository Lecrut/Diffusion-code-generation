class TruthValueManager:
    TRUE = True
    FALSE = False

    @staticmethod
    def get_opposite(value):
        return not value

if __name__ == '__main__':
    manager = TruthValueManager()
    sample_value1 = True
    sample_value2 = False
    print(f"Opposite of {sample_value1} is {manager.get_opposite(sample_value1)}")
    print(f"Opposite of {sample_value2} is {manager.get_opposite(sample_value2)}")