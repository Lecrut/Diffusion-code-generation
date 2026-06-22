class Volume:
    def __init__(self, cubic_centimeters):
        self._cc = float(cubic_centimeters)

    @property
    def cubic_centimeters(self):
        return self._cc

    def to_liters(self):
        return self._cc / 1000.0

    def to_milliliters(self):
        return self._cc

    def to_gallons(self):
        return self._cc / 3785.411784

    def to_cubic_meters(self):
        return self._cc / 1000000.0

    def __str__(self):
        return f"{self._cc} cc"

if __name__ == '__main__':
    v = Volume(5000)
    print(v.to_liters())
    print(v.to_milliliters())
    print(v.to_gallons())
    print(v.to_cubic_meters())