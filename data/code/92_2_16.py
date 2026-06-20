class TruthValueManager:
    def is_valid_value(self, value):
        return isinstance(value, bool)

    def get_opposite(self, value):
        if not self.is_valid_value(value):
            raise ValueError("Input must be a boolean value")
        return not value

if __name__ == '__main__':
    manager = TruthValueManager()
    sample_value1 = True
    sample_value2 = False
    print(f"Opposite of {sample_value1} is {manager.get_opposite(sample_value1)}")
    print(f"Opposite of {sample_value2} is {manager.get_opposite(sample_value2)}")