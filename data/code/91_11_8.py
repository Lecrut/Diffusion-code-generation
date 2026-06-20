class BooleanNegator:
    def __init__(self, value: bool):
        self.value = value
    
    def negate(self) -> bool:
        self.value = not self.value

if __name__ == '__main__':
    negator1 = BooleanNegator(True)
    print(negator1.value)  # Output: True
    negator1.negate()
    print(negator1.value)  # Output: False
    
    negator2 = BooleanNegator(False)
    print(negator2.value)  # Output: False
    negator2.negate()
    print(negator2.value)  # Output: True