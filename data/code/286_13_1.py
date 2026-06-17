class UnitConverter:
    def convert_meters_to_feet(self, meters):
        return meters * 3.28084
    def convert_feet_to_meters(self, feet):
        return feet / 3.28084
if __name__ == '__main__':
    converter = UnitConverter()
    meters_value = 10
    feet_result = converter.convert_meters_to_feet(meters_value)
    print(f"{meters_value} meters is equal to {feet_result:.2f} feet")
    feet_value = 50
    meters_result = converter.convert_feet_to_meters(feet_value)
    print(f"{feet_value} feet is equal to {meters_result:.2f} meters")