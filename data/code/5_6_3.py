class ImpossibleLengthError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.detail = message

LENGTH_THRESHOLD = 1e12

class LengthPair:
    def __init__(self, value_x, value_y):
        self.value_x = value_x
        self.value_y = value_y

    def _check_negativity(self):
        if self.value_x < 0:
            raise ImpossibleLengthError(f"Value X is negative: {self.value_x}")
        if self.value_y < 0:
            raise ImpossibleLengthError(f"Value Y is negative: {self.value_y}")

    def _check_impossibility(self):
        if self.value_x > LENGTH_THRESHOLD or self.value_y > LENGTH_THRESHOLD:
            raise ImpossibleLengthError("Difference between lengths exceeds physical limits")

    def analyze(self):
        self._check_negativity()
        self._check_impossibility()
        difference = abs(self.value_x - self.value_y)
        ratio = self.value_x / self.value_y if self.value_y != 0 else float('inf')
        return difference, ratio

if __name__ == '__main__':
    sample_a = LengthPair(50.0, 12.5)
    sample_b = LengthPair(100, -5)
    
    result_good = sample_a.analyze()
    print(result_good)
    
    try:
        result_bad = sample_b.analyze()
        print(result_bad)
    except ImpossibleLengthError as error:
        print(error.detail)