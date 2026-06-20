class TruthValueManager:
    def get_opposite(self, value):
        return not value

if __name__ == '__main__':
    manager = TruthValueManager()
    sample_values = {True: "True", False: "False"}
    for sample_value in sample_values:
        opposite_value = manager.get_opposite(sample_value)
        print(f"Opposite of {sample_values[sample_value]} is {opposite_value}")