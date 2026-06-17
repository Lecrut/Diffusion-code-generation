class UnitConverter:
    def convert_length(self, value, from_unit, to_unit):
        if from_unit == "m":
            if to_unit == "ft":
                return value * 3.28084
            elif to_unit == "km":
                return value / 1000
            elif to_unit == "m":
                return value
        elif from_unit == "ft":
            if to_unit == "m":
                return value * 0.3048
            elif to_unit == "km":
                return value * 0.0003048
            elif to_unit == "ft":
                return value
        elif from_unit == "km":
            if to_unit == "m":
                return value * 1000
            elif to_unit == "ft":
                return value * 3280.84
            elif to_unit == "km":
                return value
        else:
            raise ValueError("Invalid starting unit")
if __name__ == '__main__':
    converter = UnitConverter()
    meters = 10
    feet = converter.convert_length(meters, "m", "ft")
    print(f"{meters} meters is equal to {feet:.4f} feet")
    feet_val = 5
    meters_val = converter.convert_length(feet_val, "ft", "m")
    print(f"{feet_val} feet is equal to {meters_val:.4f} meters")
    km_val = 2.5
    meters_from_km = converter.convert_length(km_val, "km", "m")
    print(f"{km_val} kilometers is equal to {meters_from_km:.4f} meters")
    km_to_ft = converter.convert_length(1, "km", "ft")
    print(f"1 kilometer is equal to {km_to_ft:.4f} feet")