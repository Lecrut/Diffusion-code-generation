class TruthValueManager:
    def get_opposite(self, value):
        return not value

if __name__ == '__main__':
    manager = TruthValueManager()
    sample_values = [True, False]
    for val in sample_values:
        print(f"Opposite of {val} is {manager.get_opposite(val)}")