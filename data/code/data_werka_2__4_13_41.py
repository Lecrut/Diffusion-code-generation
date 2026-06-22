class DistanceConverter:
    def __init__(self):
        self.miles_to_feet = 5280

    def miles_to_feet_conversion(self, miles):
        return miles * self.miles_to_feet

    def feet_to_miles_conversion(self, feet):
        return feet / self.miles_to_feet

if __name__ == '__main__':
    converter = DistanceConverter()
    
    sample_miles = 5
    converted_feet = converter.miles_to_feet_conversion(sample_miles)
    print(f"{sample_miles} miles is {converted_feet} feet")
    
    sample_feet = 10000
    converted_miles = converter.feet_to_miles_conversion(sample_feet)
    print(f"{sample_feet} feet is {converted_miles} miles")