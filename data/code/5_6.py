class ImpossibleLengthError(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)
        self.message = message

class LengthComparator:
    def __init__(self, length_a, length_b):
        self.length_a = length_a
        self.length_b = length_b

    def compare(self):
        if self.length_a < 0 or self.length_b < 0:
            raise ImpossibleLengthError("Length cannot be negative")
        if self.length_a > self.length_b:
            return self.length_a - self.length_b
        return self.length_b - self.length_a

if __name__ == '__main__':
    try:
        comparator = LengthComparator(10, 5)
        result = comparator.compare()
        print(result)
    except ImpossibleLengthError:
        print("Caught exception")
    try:
        comparator_invalid = LengthComparator(-5, 5)
        result_invalid = comparator_invalid.compare()
        print(result_invalid)
    except ImpossibleLengthError:
        print("Caught exception for invalid input")