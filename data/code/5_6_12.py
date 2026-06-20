class LengthComparisonError(Exception):
    def __init__(self, message):
        super().__init__(message)

class LengthObject:
    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2

    def validate_lengths(self):
        if self.length1 < 0 or self.length2 < 0:
            raise LengthComparisonError("Lengths cannot be negative")
        if abs(self.length1 - self.length2) > max(self.length1, self.length2) * 1000:
            raise LengthComparisonError("Lengths are impossibly different")
        return True

if __name__ == '__main__':
    obj1 = LengthObject(5, 10)
    try:
        result1 = obj1.validate_lengths()
        print(result1)
    except LengthComparisonError as e:
        print(str(e))

    obj2 = LengthObject(-5, 10)
    try:
        result2 = obj2.validate_lengths()
        print(result2)
    except LengthComparisonError as e:
        print(str(e))

    obj3 = LengthObject(1, 1000000)
    try:
        result3 = obj3.validate_lengths()
        print(result3)
    except LengthComparisonError as e:
        print(str(e))