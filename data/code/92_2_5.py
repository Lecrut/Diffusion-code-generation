class TruthValueManager:
    def get_opposite(self, value):
        return not value

if __name__ == '__main__':
    manager = TruthValueManager()
    sample_values = {True: "True", False: "False"}
    for key in sample_values:
        print(f"Opposite of {sample_values[key]} is {manager.get_opposite(key)}")