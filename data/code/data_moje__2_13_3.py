class Volume:
    def __init__(self, cubic_centimeters=0.0):
        self._cc = cubic_centimeters

    @property
    def cubic_centimeters(self):
        return self._cc

    @cubic_centimeters.setter
    def cubic_centimeters(self, value):
        self._cc = float(value)

    @property
    def liters(self):
        return self._cc / 1000.0

    @liters.setter
    def liters(self, value):
        self._cc = float(value) * 1000.0

    @property
    def milliliters(self):
        return self._cc

    @milliliters.setter
    def milliliters(self, value):
        self._cc = float(value)

    @property
    def gallons(self):
        return self._cc / 3785.411784

    @gallons.setter
    def gallons(self, value):
        self._cc = float(value) * 3785.411784

    @property
    def cubic_meters(self):
        return self._cc / 1000000.0

    @cubic_meters.setter
    def cubic_meters(self, value):
        self._cc = float(value) * 1000000.0

    def __add__(self, other):
        if isinstance(other, Volume):
            return Volume(self._cc + other._cc)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Volume):
            return Volume(self._cc - other._cc)
        return NotImplemented

    def __mul__(self, factor):
        return Volume(self._cc * float(factor))

    def __truediv__(self, divisor):
        return Volume(self._cc / float(divisor))

    def __eq__(self, other):
        if isinstance(other, Volume):
            return self._cc == other._cc
        return NotImplemented

    def __repr__(self):
        return f"Volume({self._cc})"

if __name__ == '__main__':
    v1 = Volume(liters=1.5)
    v2 = Volume(milliliters=500.0)
    
    print(f"Volume 1 in cc: {v1.cubic_centimeters}")
    print(f"Volume 1 in gallons: {v1.gallons}")
    print(f"Volume 1 in cubic meters: {v1.cubic_meters}")
    
    print(f"Volume 2 in liters: {v2.liters}")
    print(f"Volume 2 in gallons: {v2.gallons}")
    
    v_sum = v1 + v2
    print(f"Sum volume in liters: {v_sum.liters}")
    
    v_prod = v1 * 2.5
    print(f"V1 multiplied by 2.5 in cc: {v_prod.cubic_centimeters}")
    
    v_gal = Volume(gallons=1.0)
    print(f"1 gallon in liters: {v_gal.liters}")
    
    v_cm3 = Volume(cubic_meters=0.001)
    print(f"0.001 cubic meters in cc: {v_cm3.cubic_centimeters}")