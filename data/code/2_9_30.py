class Volume:

    def __init__(self, cubic_centimeters):
        self.cubic_centimeters = cubic_centimeters

    def to_liters(self):
        return self.cubic_centimeters / 1000.0

    def to_milliliters(self):
        return self.cubic_centimeters * 1000.0

    def to_gallons(self):
        return self.cubic_centimeters * 0.000264172

    def to_cubic_meters(self):
        return self.cubic_centimeters / 1000000.0
if __name__ == '__main__':
    volume_cc = Volume(500)
    print('Liters:', volume_cc.to_liters())
    print('Milliliters:', volume_cc.to_milliliters())
    print('Gallons:', volume_cc.to_gallons())
    print('Cubic Meters:', volume_cc.to_cubic_meters())