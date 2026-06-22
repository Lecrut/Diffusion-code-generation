class LengthConverter:
    def __init__(self):
        self.factor = 1.60934

    def miles_to_kilometers(self, miles):
        if miles > 0:
            return miles * self.factor
        else:
            return 0

if __name__ == '__main__':
    converter = LengthConverter()
    sample_miles = 5
    kilometers = converter.miles_to_kilometers(sample_miles)
    print(f"Sample Miles: {sample_miles} miles")
    if kilometers is not None:
        print(f"Equivalent in Kilometers: {kilometers:.4f} km")