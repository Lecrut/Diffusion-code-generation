class LengthConverter:
    MILES_TO_KILOMETERS = 1.60934

    @staticmethod
    def convert_miles_to_kilometers(miles):
        if miles > 0:
            return miles * LengthConverter.MILES_TO_KILOMETERS
        else:
            return 0

if __name__ == '__main__':
    sample_miles = 10
    kilometers = LengthConverter.convert_miles_to_kilometers(sample_miles)
    print(f"{sample_miles} miles is equal to {kilometers:.4f} kilometers")