class VolumeConverter:
    def convert_liters_to_milliliters(self, liters):
        return liters * 1000
    def convert_milliliters_to_liters(self, milliliters):
        return milliliters / 1000
    def convert_cubic_meters_to_cubic_inches(self, cubic_meters):
        return cubic_meters * 155000.30668
    def convert_cubic_inches_to_cubic_meters(self, cubic_inches):
        return cubic_inches / 155000.30668
if __name__ == '__main__':
    converter = VolumeConverter()
    liters_value = 5.5
    milliliters_result = converter.convert_liters_to_milliliters(liters_value)
    print(f"{liters_value} liters is equal to {milliliters_result} milliliters")
    milliliters_value = 1500
    liters_result = converter.convert_milliliters_to_liters(milliliters_value)
    print(f"{milliliters_value} milliliters is equal to {liters_result} liters")
    cubic_meters_value = 1.0
    cubic_inches_result = converter.convert_cubic_meters_to_cubic_inches(cubic_meters_value)
    print(f"{cubic_meters_value} cubic meters is equal to {cubic_inches_result} cubic inches")
    cubic_inches_value = 100000.30668
    cubic_meters_result = converter.convert_cubic_inches_to_cubic_meters(cubic_inches_value)
    print(f"{cubic_inches_value} cubic inches is equal to {cubic_meters_result} cubic meters")