class DistanceConverter:
    MILES_TO_FEET = 5280

    def miles_to_feet(self, miles):
        return miles * self.MILES_TO_FEET

    def feet_to_miles(self, feet):
        return feet / self.MILES_TO_FEET

if __name__ == '__main__':
    converter = DistanceConverter()
    sample_miles = 2.5
    sample_feet = 10560
    converted_feet = converter.miles_to_feet(sample_miles)
    converted_miles = converter.feet_to_miles(sample_feet)
    print(f"{sample_miles} miles is {converted_feet} feet")
    print(f"{sample_feet} feet is {converted_miles} miles")