class TruthValueManager:
    def get_opposite(self, value):
        return not value

if __name__ == '__main__':
    manager = TruthValueManager()
    sample_values = [True, False]
    for value in sample_values:
        print(f"Opposite of {value} is {manager.get_opposite(value)}")