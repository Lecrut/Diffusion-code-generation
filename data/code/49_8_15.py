class LengthComparison:
    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2

    def compare(self):
        try:
            if not isinstance(self.length1, (int, float)) or not isinstance(self.length2, (int, float)):
                raise ValueError("Both lengths must be numbers.")
            return self.length1 < self.length2
        except ValueError as e:
            return str(e)

if __name__ == '__main__':
    comparison1 = LengthComparison(5, 10)
    print(comparison1.compare())
    
    comparison2 = LengthComparison(10, 5)
    print(comparison2.compare())
    
    comparison3 = LengthComparison(7, 7)
    print(comparison3.compare())
    
    comparison4 = LengthComparison(3.5, 2.8)
    print(comparison4.compare())
    
    comparison5 = LengthComparison('a', 10)
    print(comparison5.compare())