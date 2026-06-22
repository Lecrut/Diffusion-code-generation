class Volume:
    def __init__(self, value):
        self.value = value

    def to_liters(self):
        return self.value / 1000.0

    def to_milliliters(self):
        return self.value * 1000.0

    def to_gallons(self):
        return self.value * 0.000264172052

    def to_cubic_meters(self):
        return self.value * 1.0e-6

    def add(self, other):
        if not isinstance(other, Volume):
            raise TypeError("Can only add Volume objects")
        return Volume(self.value + other.value)

    def subtract(self, other):
        if not isinstance(other, Volume):
            raise TypeError("Can only subtract Volume objects")
        return Volume(self.value - other.value)

    def multiply(self, factor):
        return Volume(self.value * factor)

    def __repr__(self):
        return f"Volume({self.value})"

if __name__ == '__main__':
    vol1 = Volume(5000)
    vol2 = Volume(2000)
    vol_liters = vol1.to_liters()
    vol_milliliters = vol1.to_milliliters()
    vol_gallons = vol1.to_gallons()
    vol_cubic_meters = vol1.to_cubic_meters()
    vol_sum = vol1.add(vol2)
    vol_diff = vol1.subtract(vol2)
    vol_scaled = vol1.multiply(2.5)
    print(f"Liters: {vol_liters}")
    print(f"Milliliters: {vol_milliliters}")
    print(f"Gallons: {vol_gallons}")
    print(f"Cubic Meters: {vol_cubic_meters}")
    print(f"Sum: {vol_sum}")
    print(f"Difference: {vol_diff}")
    print(f"Scaled: {vol_scaled}")