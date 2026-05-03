class LengthComparisonError(Exception):
    pass
class SimpleObject:
    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2
    def compare_lengths(self):
        if self.length1 < 0 or self.length2 < 0:
            raise LengthComparisonError("One or both lengths are negative.")
        if abs(self.length1 - self.length2) > 1000:
            raise LengthComparisonError("Lengths are impossibly different.")
if __name__ == '__main__':
    obj1 = SimpleObject(10, 12)
    try:
        obj1.compare_lengths()
        print("Comparison successful for (10, 12)")
    except LengthComparisonError as e:
        print(f"Error: {e}")
    obj2 = SimpleObject(-5, 10)
    try:
        obj2.compare_lengths()
        print("Comparison successful for (-5, 10)")
    except LengthComparisonError as e:
        print(f"Error: {e}")
    obj3 = SimpleObject(10000, 10)
    try:
        obj3.compare_lengths()
        print("Comparison successful for (10000, 10)")
    except LengthComparisonError as e:
        print(f"Error: {e}")