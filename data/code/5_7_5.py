class LengthError(Exception):
    pass
class Shape:
    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2
    def compare_lengths(self):
        if self.length1 < 0 or self.length2 < 0:
            raise LengthError("One or both lengths cannot be negative.")
        if abs(self.length1 - self.length2) > 1000000:
            raise LengthError("Lengths are impossibly different.")
if __name__ == '__main__':
    shape1 = Shape(10, 5)
    try:
        shape1.compare_lengths()
        print("Lengths are valid.")
    except LengthError as e:
        print(f"Error: {e}")
    shape2 = Shape(-5, 10)
    try:
        shape2.compare_lengths()
        print("Lengths are valid.")
    except LengthError as e:
        print(f"Error: {e}")
    shape3 = Shape(10, 5000000)
    try:
        shape3.compare_lengths()
        print("Lengths are valid.")
    except LengthError as e:
        print(f"Error: {e}")