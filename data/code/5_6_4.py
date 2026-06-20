class LengthError(Exception):
    def __init__(self, message):
        super().__init__(message)

class Measurement:
    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2

    def compare_lengths(self):
        if self.length1 < 0 or self.length2 < 0:
            raise LengthError("Lengths cannot be negative")
        if abs(self.length1 - self.length2) > max(self.length1, self.length2) * 2:
            raise LengthError("Lengths are impossibly different")
        return self.length1 >= self.length2

if __name__ == '__main__':
    try:
        m1 = Measurement(10, 5)
        print(m1.compare_lengths())

        m2 = Measurement(-1, 5)
        print(m2.compare_lengths())
    except LengthError as e:
        print(repr(e))