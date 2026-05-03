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
        return None
if __name__ == '__main__':
    print("--- Length Conversion ---")
    length_m = 10
    length_ft = UnitConverter.to_imperial(length_m, 'meter')
    print(f"{length_m} meters is approximately {length_ft} feet")
    print("\n--- Mass Conversion ---")
    mass_kg = 5
    mass_lb = UnitConverter.to_imperial(mass_kg, 'kilogram')
    print(f"{mass_kg} kilograms is approximately {mass_lb} pounds")
    print("\n--- Volume Conversion ---")
    volume_l = 2
    volume_gal = UnitConverter.to_imperial(volume_l, 'liter')
    print(f"{volume_l} liters is approximately {volume_gal} gallons")