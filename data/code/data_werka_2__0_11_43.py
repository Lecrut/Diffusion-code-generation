class DistanceConverter:
    def __init__(self):
        self.conversion_factor = 5

    def kilometers_to_miles(self, kilometers):
        if not isinstance(kilometers, (int, float)):
            raise ValueError("Distance must be a number")
        return kilometers * self.conversion_factor

if __name__ == '__main__':
    converter = DistanceConverter()
    sample_kilometers = 20
    miles = converter.kilometers_to_miles(sample_kilometers)
    print(miles)