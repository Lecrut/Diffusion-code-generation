class DistanceConverter:
    _MILES_TO_KM = 1.60934
    _KM_TO_MILES = 1 / 1.60934
    _MILES_TO_METERS = 1.60934 * 1000
    _METERS_TO_MILES = 1 / (1.60934 * 1000)
    _KM_TO_METERS = 1000
    _METERS_TO_KM = 1 / 1000

    def convert(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        
        if from_unit == "miles" and to_unit == "kilometers":
            return value * self._MILES_TO_KM
        
        if from_unit == "kilometers" and to_unit == "miles":
            return value * self._KM_TO_MILES
        
        if from_unit == "miles" and to_unit == "meters":
            return value * self._MILES_TO_METERS
        
        if from_unit == "meters" and to_unit == "miles":
            return value * self._METERS_TO_MILES
        
        if from_unit == "kilometers" and to_unit == "meters":
            return value * self._KM_TO_METERS
        
        if from_unit == "meters" and to_unit == "kilometers":
            return value * self._METERS_TO_KM
        
        raise ValueError(f"Conversion between '{from_unit}' and '{to_unit}' is not supported.")

if __name__ == '__main__':
    converter = DistanceConverter()
    result = converter.convert(5.0, "miles", "kilometers")
    print(result)
    result2 = converter.convert(100, "kilometers", "meters")
    print(result2)
    result3 = converter.convert(1500, "meters", "miles")
    print(result3)