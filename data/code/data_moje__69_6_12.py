MILES_TO_FEET = 5280

class MilesConverter:
    def __init__(self, factor):
        self._factor = factor

    def convert(self, miles):
        return miles * self._factor

if __name__ == '__main__':
    converter = MilesConverter(MILES_TO_FEET)
    result1 = converter.convert(1)
    print(result1)
    result2 = converter.convert(5)
    print(result2)
    result3 = converter.convert(0.5)
    print(result3)