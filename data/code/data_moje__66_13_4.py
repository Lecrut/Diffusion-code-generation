class LengthConverter:
    KILOMETERS_TO_METERS = 1000

    @staticmethod
    def km_to_meters(km):
        return km * LengthConverter.KILOMETERS_TO_METERS

if __name__ == '__main__':
    sample_value = 5
    result = LengthConverter.km_to_meters(sample_value)
    print(result)