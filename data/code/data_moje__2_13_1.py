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

    @classmethod
    def from_liters(cls, liters):
        return cls(liters * 1000.0)

    @classmethod
    def from_milliliters(cls, milliliters):
        return cls(milliliters)

    @classmethod
    def from_gallons(cls, gallons):
        return cls(gallons * 3785.411784)

    @classmethod
    def from_cubic_meters(cls, cubic_meters):
        return cls(cubic_meters * 1000000.0)

    def __repr__(self):
        return f"Volume({self._cc} cc)"

    def __str__(self):
        return f"{self._cc} cubic centimeters"

if __name__ == '__main__':
    base_volume = Volume(2500.0)
    liters_val = base_volume.to_liters()
    gallons_val = base_volume.to_gallons()
    cubic_meters_val = base_volume.to_cubic_meters()
    derived_from_gallons = Volume.from_gallons(5.0)
    derived_liters = derived_from_gallons.to_liters()
    print(liters_val)
    print(gallons_val)
    print(cubic_meters_val)
    print(derived_liters)