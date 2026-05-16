class VolumeConverter:
    def convert_liters_to_milliliters(self, liters):
        return liters * 1000
    def convert_milliliters_to_liters(self, milliliters):
        return milliliters / 1000
    def convert_cubic_meters_to_cubic_inches(self, cubic_meters):
        conversion_factor = 35314.6667
        return cubic_meters * conversion_factor
    def convert_cubic_inches_to_cubic_meters(self, cubic_inches):
        conversion_factor = 0.0264172
        return cubic_inches * conversion_factor
if __name__ == '__main__':
    converter = VolumeConverter()
    print("--- Liters to Milliliters Conversion ---")
    liters_value = 5.5
    milliliters = converter.convert_liters_to_milliliters(liters_value)
    print(f"{liters_value} Liters is equal to {milliliters} Milliliters")
    liters_value = 123.45
    milliliters = converter.convert_liters_to_milliliters(liters_value)
    print(f"{liters_value} Liters is equal to {milliliters} Milliliters")
    print("\n--- Cubic Meters to Cubic Inches Conversion ---")
    cubic_meters_value = 1.0
    cubic_inches = converter.convert_cubic_meters_to_cubic_inches(cubic_meters_value)
    print(f"{cubic_meters_value} Cubic Meters is equal to {cubic_inches} Cubic Inches")
    cubic_meters_value = 2.5
    cubic_inches = converter.convert_cubic_meters_to_cubic_inches(cubic_meters_value)
    print(f"{cubic_meters_value} Cubic Meters is equal to {cubic_inches} Cubic Inches")
    print("\n--- Cubic Inches to Cubic Meters Conversion ---")
    cubic_inches_value = 10000
    cubic_meters = converter.convert_cubic_inches_to_cubic_meters(cubic_inches_value)
    print(f"{cubic_inches_value} Cubic Inches is equal to {cubic_meters} Cubic Meters")
    cubic_inches_value = 50000
    cubic_meters = converter.convert_cubic_inches_to_cubic_meters(cubic_inches_value)
    print(f"{cubic_inches_value} Cubic Inches is equal to {cubic_meters} Cubic Meters")