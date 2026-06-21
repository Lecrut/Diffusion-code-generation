class DistanceConverter:
    def __init__(self):
        self.conversion_factor = 5

    def kilometers_to_miles(self, kilometers):
        return kilometers * self.conversion_factor

if __name__ == '__main__':
    converter = DistanceConverter()
    sample_kilometers1 = 20
    miles1 = converter.kilometers_to_miles(sample_kilometers1)
    print(miles1)

    sample_kilometers2 = 25
    miles2 = converter.kilometers_to_miles(sample_kilometers2)
    print(miles2)