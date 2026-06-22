class LengthValidationError(Exception):
    def __init__(self, message):
        super().__init__(message)

class MeasurementObject:
    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2

    def compare_lengths(self):
        if self.length1 < 0 or self.length2 < 0:
            raise LengthValidationError("Lengths cannot be negative")
        if abs(self.length1 - self.length2) > 1000:
            raise LengthValidationError("Lengths are impossibly different")
        return abs(self.length1 - self.length2)

if __name__ == '__main__':
    obj = MeasurementObject(10, 20)
    print(obj.compare_lengths())
    obj_invalid = MeasurementObject(-5, 10)
    try:
        print(obj_invalid.compare_lengths())
    except LengthValidationError as e:
        print(str(e))
    obj_impossible = MeasurementObject(10, 10000)
    try:
        print(obj_impossible.compare_lengths())
    except LengthValidationError as e:
        print(str(e))