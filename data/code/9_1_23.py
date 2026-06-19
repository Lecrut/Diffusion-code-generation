class VolumeConverter:

    def liters_to_milliliters(self, liters):
        return liters * 1000

    def milliliters_to_liters(self, milliliters):
        return milliliters / 1000

    def cubic_meters_to_cubic_inches(self, cubic_meters):
        return cubic_meters * 61023.7441

    def cubic_inches_to_cubic_meters(self, cubic_inches):
        return cubic_inches / 61023.7441
if __name__ == '__main__':
    converter = VolumeConverter()
    liters = 5
    milliliters = converter.liters_to_milliliters(liters)
    print(f'{liters} liters is {milliliters} milliliters')
    milliliters = 2000
    liters = converter.milliliters_to_liters(milliliters)
    print(f'{milliliters} milliliters is {liters} liters')
    cubic_meters = 1
    cubic_inches = converter.cubic_meters_to_cubic_inches(cubic_meters)
    print(f'{cubic_meters} cubic meters is {cubic_inches} cubic inches')
    cubic_inches = 1000
    cubic_meters = converter.cubic_inches_to_cubic_meters(cubic_inches)
    print(f'{cubic_inches} cubic inches is {cubic_meters} cubic meters')