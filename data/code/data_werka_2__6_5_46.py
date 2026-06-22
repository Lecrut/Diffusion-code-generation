class Weight:
    UNIT = "kg"
    
    def __init__(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Weight must be a number.")
        self.value = value
    
    @staticmethod
    def calculate_difference(weight1, weight2):
        return abs(weight1.value - weight2.value)

if __name__ == '__main__':
    w1 = Weight(70)
    w2 = Weight(60)
    print(f"Difference: {Weight.calculate_difference(w1, w2)} {Weight.UNIT}")