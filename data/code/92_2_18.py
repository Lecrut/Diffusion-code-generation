class TruthValueManager:
    def get_opposite(self, value):
        return not value

if __name__ == '__main__':
    manager = TruthValueManager()
    sample_value1 = True
    print(f"Opposite of {sample_value1} is {manager.get_opposite(sample_value1)}")