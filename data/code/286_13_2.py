class UnitConverter:
    def convert_meters_to_feet(self, meters):
        return meters * 3.28084
    def convert_feet_to_meters(self, feet):
        return feet / 3.28084
if __name__ == '__main__':
    converter = UnitConverter()
    meters_value = 10
    feet_value = 32.8084
    feet_from_meters = converter.convert_meters_to_feet(meters_value)
    meters_from_feet = converter.convert_feet_to_meters(feet_value)
    print(f"{meters_value} meters is equal to {feet_from_meters:.4f} feet")
    print(f"{feet_value} feet is equal to {meters_from_feet:.4f} meters")