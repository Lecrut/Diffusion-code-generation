class ImpossibleLengthException(Exception):
    def __init__(self, msg):
        Exception.__init__(self, msg)
        self.msg = msg

class Measurement:
    def __init__(self, primary, secondary):
        self.primary = primary
        self.secondary = secondary

    def validate_lengths(self):
        if self.primary < 0:
            raise ImpossibleLengthException("Primary length is negative")
        if self.secondary < 0:
            raise ImpossibleLengthException("Secondary length is negative")
        return True

    def get_difference(self):
        self.validate_lengths()
        return abs(self.primary - self.secondary)

if __name__ == '__main__':
    m = Measurement(100, 50)
    diff = m.get_difference()
    print(diff)

    m2 = Measurement(-10, 50)
    try:
        m2.get_difference()
    except ImpossibleLengthException as e:
        print(e.msg)