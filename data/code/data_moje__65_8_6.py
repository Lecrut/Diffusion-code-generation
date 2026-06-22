class FeetToInches:
    INCHES_PER_FOOT = 12

    @staticmethod
    def convert(feet):
        return feet * FeetToInches.INCHES_PER_FOOT

if __name__ == '__main__':
    converter = FeetToInches()
    test_input = 12
    result = converter.convert(test_input)
    assert result == 144
    print(result)