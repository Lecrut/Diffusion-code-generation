import math

class NumberDifference:
    def __init__(self):
        self.value1 = 42
        self.value2 = 24
    
    def get_signed_difference(self) -> int:
        return self.value1 - self.value2

if __name__ == '__main__':
    difference_instance = NumberDifference()
    print(f"Signed Difference: {difference_instance.get_signed_difference()}")