class VolumeMeasurement:
    def __init__(self, cc=0.0):
        self._cc = float(cc)

    def _normalize_cc(self, value):
        return float(value)

    def get_cubic_centimeters(self):
        return self._cc

    def get_liters(self):
        return self._cc / 1000.0

    def get_milliliters(self):
        return self._cc * 1000.0

    def get_gallons(self):
        return self._cc * 0.000264172052

    def get_cubic_meters(self):
        return self._cc * 0.000001

    @classmethod
    def from_liters(cls, liters):
        return cls(liters * 1000.0)

    @classmethod
    def from_milliliters(cls, ml):
        return cls(ml / 1000.0)

    @classmethod
    def from_gallons(cls, gallons):
        return cls(gallons / 0.000264172052)

    @classmethod
    def from_cubic_meters(cls, m3):
        return cls(m3 / 0.000001)

    def to_cubic_centimeters(self):
        return self._cc

    def to_liters(self):
        return self._cc / 1000.0

    def to_milliliters(self):
        return self._cc * 1000.0

    def to_gallons(self):
        return self._cc * 0.000264172052

    def to_cubic_meters(self):
        return self._cc * 0.000001

    def add(self, other):
        if isinstance(other, VolumeMeasurement):
            return VolumeMeasurement(self._cc + other._cc)
        return VolumeMeasurement(self._cc + other)

    def subtract(self, other):
        if isinstance(other, VolumeMeasurement):
            return VolumeMeasurement(self._cc - other._cc)
        return VolumeMeasurement(self._cc - other)

    def multiply(self, factor):
        return VolumeMeasurement(self._cc * factor)

    def divide(self, divisor):
        return VolumeMeasurement(self._cc / divisor)

    def __repr__(self):
        return f"VolumeMeasurement(cc={self._cc})"

    def __str__(self):
        return f"{self._cc} cc"

if __name__ == '__main__':
    vol = VolumeMeasurement.from_liters(1.5)
    print(vol.get_liters())
    print(vol.get_milliliters())
    print(vol.get_gallons())
    print(vol.get_cubic_meters())