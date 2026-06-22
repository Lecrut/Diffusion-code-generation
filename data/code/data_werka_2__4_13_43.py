class DistanceConverter:
    MILES_TO_FEET = 5280

    @staticmethod
    def miles_to_feet(miles):
        return miles * DistanceConverter.MILES_TO_FEET

    @staticmethod
    def feet_to_miles(feet):
        return feet / DistanceConverter.MILES_TO_FEET

if __name__ == '__main__':
    sample_miles = 2.5
    sample_feet = 10000
    converted_feet = DistanceConverter.miles_to_feet(sample_miles)
    converted_miles = DistanceConverter.feet_to_miles(sample_feet)
    print(f"{sample_miles} miles is {converted_feet} feet")
    print(f"{sample_feet} feet is {converted_miles} miles")