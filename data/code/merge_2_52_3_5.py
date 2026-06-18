import sys
class YieldUntilFinal:
    def __init__(self, data):
        self.data = iter(data)
    def generate(self):
        try:
            while True:
                value = next(self.data)
                yield value
                if isinstance(value, int) and value > 10 and value % 2 == 0:
                    break
        except StopIteration:
            pass
if __name__ == '__main__':
    sample_stream = [3, 7, 5, 9, 4, 8, 6]
    generator = YieldUntilFinal(sample_stream)
    for item in generator.generate():
        print(item)