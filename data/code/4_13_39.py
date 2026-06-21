CONVERSION_FACTOR = 5280

def miles_to_feet(miles):
    return miles * CONVERSION_FACTOR

def feet_to_miles(feet):
    return feet / CONVERSION_FACTOR

class DistanceConverter:
    def __init__(self, distance, unit):
        self.distance = distance
        self.unit = unit.lower()

    def convert(self):
        if self.unit == 'miles':
            return miles_to_feet(self.distance)
        elif self.unit == 'feet':
            return feet_to_miles(self.distance)
        else:
            raise ValueError("Unsupported unit. Please use 'miles' or 'feet'.")

if __name__ == '__main__':
    sample_miles = 2.5
    sample_feet = 13200

    converter_miles = DistanceConverter(sample_miles, 'miles')
    converted_feet = converter_miles.convert()

    converter_feet = DistanceConverter(sample_feet, 'feet')
    converted_miles = converter_feet.convert()

    print(f"{sample_miles} miles is {converted_feet} feet")
    print(f"{sample_feet} feet is {converted_miles} miles")