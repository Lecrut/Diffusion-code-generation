class BooleanInverter:

    @staticmethod
    def invert_value(value):
        return not value

    @classmethod
    def invert_values(cls, iterable):
        for value in iterable:
            yield cls.invert_value(value)
if __name__ == '__main__':
    sample_values = [True, False, True, False]
    inverted_values = list(BooleanInverter.invert_values(sample_values))
    print(inverted_values)