class DistanceConverter:
    MILES_TO_KILOMETERS = 1.60934
    KILOMETERS_TO_MILES = 1.0 / 1.60934
    KILOMETERS_TO_METERS = 1000.0
    METERS_TO_KILOMETERS = 1.0 / 1000.0
    MILES_TO_METERS = 1.60934 * 1000.0
    METERS_TO_MILES = 1.0 / (1.60934 * 1000.0)

    def convert(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        
        if from_unit == "miles" and to_unit == "kilometers":
            return value * self.MILES_TO_KILOMETERS
        if from_unit == "kilometers" and to_unit == "miles":
            return value * self.KILOMETERS_TO_MILES
        
        if from_unit == "kilometers" and to_unit == "meters":
            return value * self.KILOMETERS_TO_METERS
        if from_unit == "meters" and to_unit == "kilometers":
            return value * self.METERS_TO_KILOMETERS
        
        if from_unit == "miles" and to_unit == "meters":
            return value * self.MILES_TO_METERS
        if from_unit == "meters" and to_unit == "miles":
            return value * self.METERS_TO_MILES
        
        raise ValueError(f"Unsupported conversion from {from_unit} to {to_unit}")

if __name__ == '__main__':
    converter = DistanceConverter()
    
    result1 = converter.convert(5, "miles", "kilometers")
    print(result1)
    
    result2 = converter.convert(10000, "meters", "miles")
    print(result2)
    
    result3 = converter.convert(1.5, "kilometers", "meters")
    print(result3)