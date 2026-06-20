class TruthValueManager:
    def validate_input(self, value):
        if not isinstance(value, bool):
            raise ValueError("Input must be a boolean value")
    
    def get_opposite(self, value):
        self.validate_input(value)
        return not value

if __name__ == '__main__':
    manager = TruthValueManager()
    sample_value1 = True
    sample_value2 = False
    print(f"Opposite of {sample_value1} is {manager.get_opposite(sample_value1)}")
    print(f"Opposite of {sample_value2} is {manager.get_opposite(sample_value2)}")