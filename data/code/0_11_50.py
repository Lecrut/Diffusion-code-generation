KM_TO_MILES_CONVERSION_FACTOR = 5

class DistanceConverter:
    def __init__(self, conversion_factor):
        self.conversion_factor = conversion_factor

    def convert(self, kilometers):
        if not isinstance(kilometers, (int, float)):
            raise ValueError("Distance must be a number")
        return kilometers * self.conversion_factor

if __name__ == '__main__':
    converter = DistanceConverter(KM_TO_MILES_CONVERSION_FACTOR)
    sample_kilometers = 20
    miles = converter.convert(sample_kilometers)
    print(miles)