class TruthValueManager:
    def get_opposite(self, value):
        opposite_values = {True: False, False: True}
        return opposite_values[value]

if __name__ == '__main__':
    manager = TruthValueManager()
    sample_value1 = True
    sample_value2 = False
    print(f"Opposite of {sample_value1} is {manager.get_opposite(sample_value1)}")
    print(f"Opposite of {sample_value2} is {manager.get_opposite(sample_value2)}")