class UnitConverter:
    def convert_length(self, value, from_unit, to_unit):
        if from_unit == "m" and to_unit in ["ft", "km"]:
            if to_unit == "ft":
                return value * 3.28084
            elif to_unit == "km":
                return value / 1000.0
        elif from_unit == "ft" and to_unit in ["m", "km"]:
            if to_unit == "m":
                return value / 3.28084
            elif to_unit == "km":
                return value * 0.3048
        elif from_unit == "km" and to_unit in ["m", "ft"]:
            if to_unit == "m":
                return value * 1000.0
            elif to_unit == "ft":
                return value / 0.3048
        elif from_unit == to_unit:
            return value
        else:
            raise ValueError("Unsupported unit conversion")
if __name__ == '__main__':
    converter = UnitConverter()
    meters = 10.0
    feet = converter.convert_length(meters, "m", "ft")
    print(f"{meters} meters is equal to {feet} feet")
    feet_val = 32.8084
    meters_val = converter.convert_length(feet_val, "ft", "m")
    print(f"{feet_val} feet is equal to {meters_val} meters")
    km = 5.0
    meters_from_km = converter.convert_length(km, "km", "m")
    print(f"{km} kilometers is equal to {meters_from_km} meters")
    km_to_ft = 10.0
    feet_from_km = converter.convert_length(km_to_ft, "km", "ft")
    print(f"{km_to_ft} kilometers is equal to {feet_from_km} feet")
    same_unit = 50.0
    result_same = converter.convert_length(same_unit, "m", "m")
    print(f"{same_unit} meters is equal to {result_same} meters")