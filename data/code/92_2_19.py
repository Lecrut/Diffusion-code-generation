class TruthValueManager:
    def get_opposite(self, value):
        opposite_mapping = {True: False, False: True}
        return opposite_mapping[value]

if __name__ == '__main__':
    manager = TruthValueManager()
    sample_value1 = True
    sample_value2 = False
    print(f"Opposite of {sample_value1} is {manager.get_opposite(sample_value1)}")
    print(f"Opposite of {sample_value2} is {manager.get_opposite(sample_value2)}")