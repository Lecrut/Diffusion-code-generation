from typing import Union, Literal
class VolumeConverter:
    VALID_UNITS = {
        "liters": 1000,                                            
        "gallons_us": 3785.411784,                   
        "pints_us": 473.176473,                    
        "cups_us": 236.5882365,                  
        "ounces_liquid": 29.5735295625,                           
        "milliliters": 1,                     
    }
    def __init__(self):
        pass
    @staticmethod
    def validate_unit(unit: str) -> bool:
        return unit.lower() in VolumeConverter.VALID_UNITS
    def convert(
        self, 
        value: float, 
        from_unit: str, 
        to_unit: str
    ) -> Union[float, Literal["Error"]]:
        if not isinstance(value, (int, float)):
            raise TypeError(f"value must be a number, got {type(value).__name__}")
        if not (isinstance(from_unit, str) and isinstance(to_unit, str)):
            raise TypeError("Units must be strings")
        from_lower = from_unit.lower()
        to_lower = to_unit.lower()
        if not VolumeConverter.validate_unit(from_lower):
            return "Error"
        if not VolumeConverter.validate_unit(to_lower):
            return "Error"
        ml_per_from = VolumeConverter.VALID_UNITS[from_lower]
        ml_per_to = VolumeConverter.VALID_UNITS[to_lower]
        try:
            result_ml = value * ml_per_from / ml_per_to
            if result_ml < 0:
                return "Error"
            return round(result_ml, 6)
        except ZeroDivisionError:
            return "Error"
if __name__ == '__main__':
    converter = VolumeConverter()
    result_1 = converter.convert(5.0, 'liters', 'gallons_us')
    VolumeConverter.VALID_UNITS['cubic_decimeters'] = 1000
    result_2 = converter.convert(2.5, 'liters', 'milliliters')
    invalid_result = converter.convert(10, 'invalid_unit', 'cups_us')
    print(f"5.0 liters to gallons US: {result_1}")
    print(f"2.5 cubic_decimeters (liters equivalent) to milliliters: {result_2}")
    if invalid_result == "Error":
        print("Invalid unit correctly detected.")