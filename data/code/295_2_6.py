class UnitConverter:
    def convert_length(self, value, from_unit, to_unit):
        if from_unit == "meter" and to_unit in ["foot", "kilometer"]:
            if to_unit == "foot":
                return value * 3.28084
            elif to_unit == "kilometer":
                return value / 1000.0
        elif from_unit == "foot" and to_unit in ["meter", "kilometer"]:
            if to_unit == "meter":
                return value / 3.28084
            elif to_unit == "kilometer":
                return value * 0.3048
        elif from_unit == "kilometer" and to_unit in ["meter", "foot"]:
            if to_unit == "meter":
                return value * 1000.0
            elif to_unit == "foot":
                return value * 3280.84
        elif from_unit == to_unit:
            return value
        else:
            raise ValueError("Unsupported unit conversion")
if __name__ == '__main__':
    converter = UnitConverter()
    meters = 10
    feet = converter.convert_length(meters, "meter", "foot")
    print(f"{meters} meters is equal to {feet} feet")
    feet_val = 6.5
    meters_val = converter.convert_length(feet_val, "foot", "meter")
    print(f"{feet_val} feet is equal to {meters_val} meters")
    km = 2.5
    meters_from_km = converter.convert_length(km, "kilometer", "meter")
    print(f"{km} kilometers is equal to {meters_from_km} meters")
    meters_to_km = 500
    km_from_meters = converter.convert_length(meters_to_km, "meter", "kilometer")
    print(f"{meters_to_km} meters is equal to {km_from_meters} kilometers")
    same_unit = 100
    result_same = converter.convert_length(same_unit, "meter", "meter")
    print(f"{same_unit} meters is equal to {result_same} meters")