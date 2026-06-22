class VolumeConverter:
    def __init__(self):
        self._units = {
            "l": 1.0,
            "ml": 0.001,
            "m3": 1000.0,
            "gal_us": 3.785411784,
            "qt_us": 0.946352946,
            "pt_us": 0.473176473,
            "cup_us": 0.2365882365,
            "fl_oz_us": 0.0295735295625,
            "gal_uk": 4.54609,
            "qt_uk": 1.1365225,
            "pt_uk": 0.56826125,
            "fl_oz_uk": 0.0284130625,
        }

    def convert(self, value, from_unit, to_unit):
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()
        if from_unit not in self._units:
            raise ValueError(f"Unknown source unit: {from_unit}")
        if to_unit not in self._units:
            raise ValueError(f"Unknown target unit: {to_unit}")
        base_value = value * self._units[from_unit]
        result = base_value / self._units[to_unit]
        return result

if __name__ == '__main__':
    converter = VolumeConverter()
    sample_value = 5.0
    sample_from = "l"
    sample_to = "gal_us"
    result = converter.convert(sample_value, sample_from, sample_to)
    print(result)
    print(converter.convert(1.0, "m3", "l"))
    print(converter.convert(1.0, "gal_uk", "gal_us"))
    print(converter.convert(1000.0, "ml", "l"))
    print(converter.convert(1.0, "qt_us", "pt_us"))