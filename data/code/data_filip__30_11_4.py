class DecimalToBinaryConverter:
    NEGATIVE_PREFIX = "-"
    ZERO_REPRESENTATION = "0"

    def __init__(self, value):
        self.value = value

    def convert(self):
        if self.value < 0:
            return self.NEGATIVE_PREFIX + self._format_positive(abs(self.value))
        if self.value == 0:
            return self.ZERO_REPRESENTATION
        return self._format_positive(self.value)

    def _format_positive(self, number):
        return format(number, 'b')

if __name__ == '__main__':
    sample_number = 42
    converter = DecimalToBinaryConverter(sample_number)
    print(converter.convert())