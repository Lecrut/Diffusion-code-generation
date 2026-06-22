class DistanceConverter:
    FEET_PER_MILE = 5280

    @staticmethod
    def miles_to_feet(miles):
        if not isinstance(miles, (int, float)):
            raise ValueError("Miles must be a number")
        return miles * DistanceConverter.FEET_PER_MILE

    @staticmethod
    def feet_to_miles(feet):
        if not isinstance(feet, (int, float)):
            raise ValueError("Feet must be a number")
        return feet / DistanceConverter.FEET_PER_MILE

if __name__ == '__main__':
    sample_miles = 2.5
    sample_feet = 13200
    converted_feet = DistanceConverter.miles_to_feet(sample_miles)
    converted_miles = DistanceConverter.feet_to_miles(sample_feet)
    print(f"{sample_miles} miles is {converted_feet} feet")
    print(f"{sample_feet} feet is {converted_miles} miles")