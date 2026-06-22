class LengthConverter:
    METER_TO_KILOMETER = 0.001

    @staticmethod
    def meters_to_kilometers(meters):
        if meters < 0:
            raise ValueError('Negative input not allowed.')
        return meters * LengthConverter.METER_TO_KILOMETER
if __name__ == '__main__':
    converter = LengthConverter()
    print(converter.meters_to_kilometers(1500))
    print(converter.meters_to_kilometers(1000))
    try:
        print(converter.meters_to_kilometers(-500))
    except ValueError as e:
        print(e)