class WeightDifferenceCalculator:
    UNIT = 'kg'
    
    @staticmethod
    def calculate_difference(x, y):
        if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
            raise ValueError("Both inputs must be numbers.")
        return abs(x - y)
    
    @classmethod
    def formatted_difference(cls, x, y):
        difference = cls.calculate_difference(x, y)
        return f"Difference: {difference} {cls.UNIT}"

if __name__ == '__main__':
    weight1 = 80
    weight2 = 70
    print(WeightDifferenceCalculator.formatted_difference(weight1, weight2))