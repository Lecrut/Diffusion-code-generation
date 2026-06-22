class InvalidLengthError(Exception):
    def __init__(self, text):
        Exception.__init__(self, text)
        self.message_text = text

class ObjectWithLengths:
    def __init__(self, x, y):
        self.length_one = x
        self.length_two = y

    def validate_and_get_difference(self):
        if self.length_one < 0:
            raise InvalidLengthError("First length is negative")
        if self.length_two < 0:
            raise InvalidLengthError("Second length is negative")
        return abs(self.length_one - self.length_two)

if __name__ == '__main__':
    sample_obj = ObjectWithLengths(100, 50)
    print(sample_obj.validate_and_get_difference())