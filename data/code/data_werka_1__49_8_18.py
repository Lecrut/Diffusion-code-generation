class LengthComparison:
    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2

    def compare(self):
        try:
            if self.length1 < self.length2:
                return "First length is less than the second."
            elif self.length1 > self.length2:
                return "First length is greater than the second."
            else:
                return "Both lengths are equal."
        except ValueError as e:
            return f"Error: {e}"

if __name__ == '__main__':
    comparison1 = LengthComparison(5, 10)
    print(comparison1.compare())
    comparison2 = LengthComparison(10, 5)
    print(comparison2.compare())
    comparison3 = LengthComparison(7, 7)
    print(comparison3.compare())
    comparison4 = LengthComparison(3, 8)
    print(comparison4.compare())