class ImpossibleLengthException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        self.details = msg

class LengthContainer:
    def __init__(self, primary_length, secondary_length):
        self.primary_length = primary_length
        self.secondary_length = secondary_length

    def validate_and_get_difference(self):
        if self.primary_length < 0 or self.secondary_length < 0:
            raise ImpossibleLengthException("Negative lengths are physically impossible")
        if abs(self.primary_length - self.secondary_length) > 1e9:
            raise ImpossibleLengthException("Length difference exceeds maximum plausible threshold")
        return abs(self.primary_length - self.secondary_length)

if __name__ == '__main__':
    container_normal = LengthContainer(100, 50)
    print(container_normal.validate_and_get_difference())
    
    container_negative = LengthContainer(100, -50)
    try:
        container_negative.validate_and_get_difference()
    except ImpossibleLengthException as e:
        print(e.details)
        
    container_huge_diff = LengthContainer(1, 1000000001)
    try:
        container_huge_diff.validate_and_get_difference()
    except ImpossibleLengthException as e:
        print(e.details)