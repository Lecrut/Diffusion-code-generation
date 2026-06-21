def validate_input(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Input must be an integer or a float.")

class ThresholdGenerator:
    def __init__(self, threshold):
        self.threshold = threshold

    def generate(self):
        while True:
            value = yield
            validate_input(value)
            if value > self.threshold:
                yield True
            else:
                yield False

if __name__ == '__main__':
    gen = ThresholdGenerator(10).generate()
    next(gen)
    values = [5, 15, 20, 8, 12]
    results = []
    for value in values:
        results.append(gen.send(value))
    print(results)