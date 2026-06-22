class InvalidLengthError(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        self.msg_value = msg

class LengthPair:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def validate(self):
        if self.a < 0:
            raise InvalidLengthError("First length is negative")
        if self.b < 0:
            raise InvalidLengthError("Second length is negative")
        return True

    def check_diff(self):
        self.validate()
        diff = abs(self.a - self.b)
        if diff > 1e6:
            raise InvalidLengthError("Difference too large")
        return diff

def run_check(a, b):
    pair = LengthPair(a, b)
    return pair.check_diff()

if __name__ == '__main__':
    print(run_check(10, 15))
    print(run_check(100, 200))