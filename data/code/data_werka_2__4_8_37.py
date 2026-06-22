class DistanceConverter:
    def __init__(self):
        self.miles_to_kilometers_factor = 1.60934
        self.kilometers_to_miles_factor = 1 / self.miles_to_kilometers_factor

    def miles_to_kilometers(self, miles):
        if not isinstance(miles, (int, float)):
            raise ValueError("Input must be a numeric value.")
        return miles * self.miles_to_kilometers_factor

    def kilometers_to_miles(self, kilometers):
        if not isinstance(kilometers, (int, float)):
            raise ValueError("Input must be a numeric value.")
        return kilometers * self.kilometers_to_miles_factor

if __name__ == '__main__':
    converter = DistanceConverter()
    sample_miles = 5
    sample_kilometers = 10

    print(f"{sample_miles} miles is {converter.miles_to_kilometers(sample_miles)} kilometers")
    print(f"{sample_kilometers} kilometers is {converter.kilometers_to_miles(sample_kilometers)} miles")