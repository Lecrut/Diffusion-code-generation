class RepeatingSequenceGenerator:
    MAX_COUNT = 50

    def __init__(self):
        self.sequence = [1, 2, 3]
        self.count = 0

    @staticmethod
    def _yield_elements(sequence):
        for item in sequence:
            yield item

    def generate(self):
        while True:
            for element in self._yield_elements(self.sequence):
                if self.count >= self.MAX_COUNT:
                    return
                yield element
                self.count += 1

if __name__ == '__main__':
    generator = RepeatingSequenceGenerator()
    result = [next(generator.generate()) for _ in range(50)]
    print(result)