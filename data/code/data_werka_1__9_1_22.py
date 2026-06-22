class VolumeConverter:

    def liters_to_milliliters(self, liters):
        return liters * 1000

    def milliliters_to_liters(self, milliliters):
        return milliliters / 1000

    def cubic_meters_to_cubic_inches(self, cubic_meters):
        return cubic_meters * 61023.7440947

    def cubic_inches_to_cubic_meters(self, cubic_inches):
        return cubic_inches / 61023.7440947
if __name__ == '__main__':
    converter = VolumeConverter()
    liters_value = 2.5
    milliliters_value = 500
    cubic_meters_value = 1.0
    cubic_inches_value = 123456
    print(f'{liters_value} liters is {converter.liters_to_milliliters(liters_value)} milliliters')
    print(f'{milliliters_value} milliliters is {converter.milliliters_to_liters(milliliters_value)} liters')
    print(f'{cubic_meters_value} cubic meters is {converter.cubic_meters_to_cubic_inches(cubic_meters_value)} cubic inches')
    print(f'{cubic_inches_value} cubic inches is {converter.cubic_inches_to_cubic_meters(cubic_inches_value)} cubic meters')