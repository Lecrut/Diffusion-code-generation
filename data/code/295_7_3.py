class UnitConverter:
    def __init__(self, conversion_factors):
        self.conversion_factors = conversion_factors
    def convert(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        if from_unit not in self.conversion_factors or to_unit not in self.conversion_factors:
            raise ValueError("One or both units are not defined in the conversion factors.")
        if from_unit == "length" and to_unit == "length":
            return value
        elif from_unit == "mass" and to_unit == "mass":
            return value
        else:
            try:
                factor = self.conversion_factors[f"{from_unit}_to_{to_unit}"]
                return value * factor
            except KeyError:
                raise ValueError(f"Conversion factor from {from_unit} to {to_unit} is not defined.")
if __name__ == '__main__':
    conversion_data = {
        "length_to_meter": 1.0,
        "length_to_foot": 3.28084,
        "mass_to_kilogram": 1.0,
        "mass_to_pound": 2.20462,
    }
    converter = UnitConverter(conversion_data)
    try:
        value_m = 10.0
        result_ft = converter.convert(value_m, "length", "length")                                                                               
        print(f"10.0 meters to meters: {converter.convert(value_m, 'length', 'length')}")
        result_ft = converter.convert(10.0, "length", "length")                                                                   
        print(f"10.0 meters to feet: {converter.convert(10.0, 'length', 'length')}")                                                         
        result_ft = converter.convert(10.0, "length", "length")
        print(f"10.0 meters to feet: {converter.convert(10.0, 'length', 'length')}")                                                                                                             
    except ValueError as e:
        print(f"Error during length conversion test: {e}")
    try:
        value_kg = 5.0
        result_lb = converter.convert(value_kg, "mass", "mass")                      
        print(f"5.0 kilograms to pounds: {converter.convert(5.0, 'mass', 'mass')}")
        result_lb = converter.convert(5.0, "mass", "mass")
        print(f"5.0 kilograms to pounds: {converter.convert(5.0, 'mass', 'mass')}")
        result_lb = converter.convert(5.0, "mass", "mass")
        print(f"5.0 kilograms to pounds: {converter.convert(5.0, 'mass', 'mass')}")
    except ValueError as e:
        print(f"Error during mass conversion test: {e}")
    conversion_data_corrected = {
        "length_to_meter": 1.0,
        "length_to_foot": 3.28084,
        "mass_to_kilogram": 1.0,
        "mass_to_pound": 2.20462,
    }
    converter_corrected = UnitConverter(conversion_data_corrected)
    print("\n--- Corrected Tests ---")
    try:
        result_ft = converter_corrected.convert(10.0, "length", "length")                                                                                 
        print(f"10.0 meters to feet: {converter_corrected.convert(10.0, 'length', 'length')}")
        result_lb = converter_corrected.convert(5.0, "mass", "mass")                                                                                 
        print(f"5.0 kilograms to pounds: {converter_corrected.convert(5.0, 'mass', 'mass')}")
        result_ft = converter_corrected.convert(10.0, "length", "length")                                                           
        print(f"10.0 meters to feet: {converter_corrected.convert(10.0, 'length', 'length')}")
        result_lb = converter_corrected.convert(5.0, "mass", "mass")                                                           
        print(f"5.0 kilograms to pounds: {converter_corrected.convert(5.0, 'mass', 'mass')}")
    except ValueError as e:
        print(f"Error during final conversion test: {e}")