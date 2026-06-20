class TruthValueManager:
    def get_opposite(self, value):
        if not isinstance(value, bool):
            raise ValueError("Input must be a boolean")
        return not value

if __name__ == '__main__':
    manager = TruthValueManager()
    sample_value1 = True
    sample_value2 = False
    print(f"Opposite of {sample_value1} is {manager.get_opposite(sample_value1)}")
    print(f"Opposite of {sample_value2} is {manager.get_opposite(sample_value2)}")