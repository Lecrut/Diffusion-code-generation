class UnitConverter:
    @staticmethod
    def to_metric(value, unit):
        if unit.lower() in ['meter', 'm', 'kilogram', 'kg', 'liter', 'l']:
            if unit.lower() in ['meter', 'm']:
                return value                                                           
            elif unit.lower() in ['kilogram', 'kg']:
                return value
            elif unit.lower() in ['liter', 'l']:
                return value
        return None
    @staticmethod
    def to_imperial(value, unit):
        if unit.lower() in ['foot', 'ft']:
            return value * 0.3048
        elif unit.lower() in ['pound', 'lb']:
            return value * 0.453592
        elif unit.lower() in ['gallon', 'gal']:
            return value * 3.78541
    @staticmethod
    def convert(value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        if from_unit.lower() in ['meter', 'm', 'kilogram', 'kg', 'liter', 'l']:
            if to_unit.lower() in ['foot', 'ft']:
                return value * 3.28084
            elif to_unit.lower() in ['pound', 'lb']:
                return value * 2.20462
            elif to_unit.lower() in ['gallon', 'gal']:
                return value * 0.264172
        if from_unit.lower() in ['foot', 'ft']:
            if to_unit.lower() in ['meter', 'm']:
                return value / 0.3048
            elif to_unit.lower() in ['pound', 'lb']:
                return value * 16.0184
        if from_unit.lower() in ['pound', 'lb']:
            if to_unit.lower() in ['foot', 'ft']:
                return value / 16.0184
            elif to_unit.lower() in ['meter', 'm']:
                return value / 0.453592
        if from_unit.lower() in ['gallon', 'gal']:
            if to_unit.lower() in ['liter', 'l']:
                return value * 3.78541
        return None
if __name__ == '__main__':
    sample_value = 10
    print("--- Length Conversion (Meter to Foot) ---")
    meter_value = 10.0
    foot_result = UnitConverter.convert(meter_value, 'meter', 'foot')
    print(f"{meter_value} meters is {foot_result:.4f} feet")
    print("\n--- Mass Conversion (Kilogram to Pound) ---")
    kg_value = 5.0
    pound_result = UnitConverter.convert(kg_value, 'kg', 'lb')
    print(f"{kg_value} kg is {pound_result:.4f} lb")
    print("\n--- Volume Conversion (Liter to Gallon) ---")
    liter_value = 10.0
    gallon_result = UnitConverter.convert(liter_value, 'l', 'gal')
    print(f"{liter_value} l is {gallon_result:.4f} gal")
    print("\n--- Direct Conversion Example (Foot to Meter) ---")
    foot_value = 10.0
    meter_result = UnitConverter.convert(foot_value, 'ft', 'm')
    print(f"{foot_value} ft is {meter_result:.4f} m")
    print("\n--- Identity Conversion Example ---")
    identity_result = UnitConverter.convert(5.0, 'm', 'm')
    print(f"5.0 m is {identity_result} m")