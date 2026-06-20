class VolumeConverter:
    def __init__(self, volume, unit):
        if unit not in ('liters', 'milliliters', 'cubic_meters', 'cubic_inches'):
            raise ValueError("Unit must be liters, milliliters, cubic_meters, or cubic_inches")
        self._volume = volume
        self._unit = unit

    @property
    def volume(self):
        return self._volume

    @property
    def unit(self):
        return self._unit

    def to_liters(self):
        if self._unit == 'liters':
            return self._volume
        elif self._unit == 'milliliters':
            return self._volume / 1000.0
        elif self._unit == 'cubic_meters':
            return self._volume * 1000.0
        elif self._unit == 'cubic_inches':
            return self._volume * 0.016387064
        return 0.0

    def to_milliliters(self):
        liters = self.to_liters()
        return liters * 1000.0

    def to_cubic_meters(self):
        if self._unit == 'cubic_meters':
            return self._volume
        elif self._unit == 'liters':
            return self._volume / 1000.0
        elif self._unit == 'milliliters':
            return self._volume / 1000000.0
        elif self._unit == 'cubic_inches':
            return self._volume * 1.6387064e-5
        return 0.0

    def to_cubic_inches(self):
        if self._unit == 'cubic_inches':
            return self._volume
        elif self._unit == 'liters':
            return self._volume / 0.016387064
        elif self._unit == 'milliliters':
            return self._volume / 0.016387064 / 1000.0
        elif self._unit == 'cubic_meters':
            return self._volume / 1.6387064e-5
        return 0.0

    def convert(self, target_unit):
        if target_unit == 'liters':
            return self.to_liters()
        elif target_unit == 'milliliters':
            return self.to_milliliters()
        elif target_unit == 'cubic_meters':
            return self.to_cubic_meters()
        elif target_unit == 'cubic_inches':
            return self.to_cubic_inches()
        raise ValueError("Target unit must be liters, milliliters, cubic_meters, or cubic_inches")

if __name__ == '__main__':
    converter = VolumeConverter(5, 'liters')
    print(converter.to_milliliters())
    print(converter.to_cubic_meters())
    
    converter2 = VolumeConverter(1, 'cubic_meters')
    print(converter2.to_cubic_inches())
    
    converter3 = VolumeConverter(1000, 'milliliters')
    print(converter3.to_liters())