class DistanceConverter:
    KILOMETER_TO_MILE = 0.621371
    MILE_TO_KILOMETER = 1.60934
    METER_TO_KILOMETER = 0.001
    KILOMETER_TO_METER = 1000
    METER_TO_MILE = 0.000621371
    MILE_TO_METER = 1609.34

    def convert(self, value, from_unit, to_unit):
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()
        
        if from_unit == to_unit:
            return value
        
        if from_unit == "kilometers" or from_unit == "km":
            if to_unit == "miles" or to_unit == "mi":
                return value * self.KILOMETER_TO_MILE
            if to_unit == "meters" or to_unit == "m":
                return value * self.KILOMETER_TO_METER
        
        if from_unit == "miles" or from_unit == "mi":
            if to_unit == "kilometers" or to_unit == "km":
                return value * self.MILE_TO_KILOMETER
            if to_unit == "meters" or to_unit == "m":
                return value * self.MILE_TO_METER
        
        if from_unit == "meters" or from_unit == "m":
            if to_unit == "kilometers" or to_unit == "km":
                return value * self.METER_TO_KILOMETER
            if to_unit == "miles" or to_unit == "mi":
                return value * self.METER_TO_MILE
        
        raise ValueError(f"Unsupported unit: {from_unit} or {to_unit}")

if __name__ == "__main__":
    converter = DistanceConverter()
    result_km_to_miles = converter.convert(100, "kilometers", "miles")
    result_miles_to_meters = converter.convert(5, "miles", "meters")
    result_meters_to_kilometers = converter.convert(1500, "meters", "kilometers")
    print(result_km_to_miles)
    print(result_miles_to_meters)
    print(result_meters_to_kilometers)