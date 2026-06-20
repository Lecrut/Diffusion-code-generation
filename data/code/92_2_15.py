class TruthValueManager:
    def get_opposite(self, value):
        return not value

if __name__ == '__main__':
    manager = TruthValueManager()
    sample_values = {True: "True", False: "False"}
    for value in sample_values.keys():
        result = manager.get_opposite(value)
        print(f"Opposite of {sample_values[value]} is {result}")