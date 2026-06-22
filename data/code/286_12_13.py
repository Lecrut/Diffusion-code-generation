class LengthConverter:
    CONVERSION_FACTOR = 1.60934

    @staticmethod
    def miles_to_kilometers(miles):
        if miles > 0:
            return miles * LengthConverter.CONVERSION_FACTOR
        else:
            return 0

if __name__ == '__main__':
    sample_miles = 5
    kilometers = LengthConverter.miles_to_kilometers(sample_miles)
    print(f"{sample_miles} miles is equal to {kilometers:.2f} kilometers")