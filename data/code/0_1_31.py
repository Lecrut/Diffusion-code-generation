class UnitConverter:
    M_TO_FEET = 3.28084
    KM_TO_M = 1000

    def meters_to_feet(self, meters):
        return meters * self.M_TO_FEET

    def feet_to_meters(self, feet):
        return feet / self.M_TO_FEET

    def kilometers_to_meters(self, kilometers):
        return kilometers * self.KM_TO_M

    def meters_to_kilometers(self, meters):
        return meters / self.KM_TO_M

if __name__ == '__main__':
    converter = UnitConverter()
    
    sample_meters = 10
    sample_feet = 30
    sample_kilometers = 2
    
    print(f"{sample_meters} meters is {converter.meters_to_feet(sample_meters)} feet")
    print(f"{sample_feet} feet is {converter.feet_to_meters(sample_feet)} meters")
    print(f"{sample_kilometers} kilometers is {converter.kilometers_to_meters(sample_kilometers)} meters")
    print(f"{sample_meters} meters is {converter.meters_to_kilometers(sample_meters)} kilometers")