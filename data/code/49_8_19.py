class LengthComparison:
    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2

    def compare(self):
        try:
            result = self.length1 < self.length2
            return f"Length {self.length1} is less than {self.length2}: {result}"
        except ValueError as e:
            return str(e)

if __name__ == '__main__':
    comparison1 = LengthComparison(5, 10)
    print(comparison1.compare())
    
    comparison2 = LengthComparison(10, 5)
    print(comparison2.compare())
    
    comparison3 = LengthComparison(7, 7)
    print(comparison3.compare())
    
    comparison4 = LengthComparison(3, 2)
    print(comparison4.compare())