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
    liters = 5.0
    milliliters = converter.liters_to_milliliters(liters)
    print(f'{liters} liters is equal to {milliliters} milliliters')
    cubic_meters = 2.0
    cubic_inches = converter.cubic_meters_to_cubic_inches(cubic_meters)
    print(f'{cubic_meters} cubic meters is equal to {cubic_inches} cubic inches')