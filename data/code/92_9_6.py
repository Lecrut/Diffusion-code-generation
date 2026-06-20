class BooleanInverter:
    def __init__(self, value: bool):
        self.value = value

    def invert(self) -> bool:
        return not self.value

if __name__ == '__main__':
    true_instance = BooleanInverter(True)
    false_instance = BooleanInverter(False)
    
    print(f"Original True: {true_instance.value}, Inverted: {true_instance.invert()}")
    print(f"Original False: {false_instance.value}, Inverted: {false_instance.invert()}")