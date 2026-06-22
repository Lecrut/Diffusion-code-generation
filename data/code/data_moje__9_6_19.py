VOLUME_UNITS = {
    "ml": 1e-6,
    "l": 1e-3,
    "m3": 1.0,
    "cup": 0.000236588,
    "fl_oz": 2.95735e-5,
    "gal": 0.00378541,
    "tbsp": 1.47868e-5,
    "tsp": 4.92892e-6,
    "bbl": 0.158987,
    "pt": 0.000473176,
    "qt": 0.000946353,
    "ft3": 0.0283168,
    "in3": 1.63871e-5,
    "yd3": 0.764555,
    "acft": 1233.48,
    "mcf": 28.3168,
    "cc": 1e-6,
    "dl": 1e-4,
    "kl": 1000.0,
    "hm3": 1000000.0
}

class VolumeConverter:
    def __init__(self, unit_factors=None):
        if unit_factors is None:
            unit_factors = VOLUME_UNITS
        self._factors = dict(unit_factors)

    def get_supported_units(self):
        return sorted(self._factors.keys())

    def convert(self, value, from_unit, to_unit):
        from_unit = from_unit.lower().strip()
        to_unit = to_unit.lower().strip()

        if from_unit not in self._factors:
            raise ValueError(
                f"Unsupported source unit: '{from_unit}'. "
                f"Supported: {self.get_supported_units()}"
            )
        if to_unit not in self._factors:
            raise ValueError(
                f"Unsupported target unit: '{to_unit}'. "
                f"Supported: {self.get_supported_units()}"
            )

        base_volume = value * self._factors[from_unit]
        result = base_volume / self._factors[to_unit]
        return result

    def register_unit(self, unit_name, factor):
        unit_name = unit_name.lower().strip()
        self._factors[unit_name] = float(factor)

    def remove_unit(self, unit_name):
        unit_name = unit_name.lower().strip()
        if unit_name in self._factors:
            del self._factors[unit_name]

def demonstrate_converter():
    converter = VolumeConverter()

    liters_to_ml = converter.convert(1, "L", "ml")
    print(f"1 L = {liters_to_ml} ml")

    cubic_meters_to_gallons = converter.convert(1, "m3", "gal")
    print(f"1 m³ = {cubic_meters_to_gallons} gal")

    gallons_to_liters = converter.convert(5, "gal", "L")
    print(f"5 gal = {gallons_to_liters} L")

    cups_to_ml = converter.convert(2, "cup", "ml")
    print(f"2 cups = {cups_to_ml} ml")

    fl_oz_to_ml = converter.convert(8, "fl_oz", "ml")
    print(f"8 fl oz = {fl_oz_to_ml} ml")

    m3_to_ft3 = converter.convert(1, "m3", "ft3")
    print(f"1 m³ = {m3_to_ft3} ft³")

    bbl_to_l = converter.convert(1, "bbl", "L")
    print(f"1 bbl = {bbl_to_l} L")

    yd3_to_m3 = converter.convert(1, "yd3", "m3")
    print(f"1 yd³ = {yd3_to_m3} m³")

    in3_to_ml = converter.convert(100, "in3", "ml")
    print(f"100 in³ = {in3_to_ml} ml")

    qt_to_cups = converter.convert(1, "qt", "cup")
    print(f"1 qt = {qt_to_cups} cups")

    pt_to_ml = converter.convert(1, "pt", "ml")
    print(f"1 pt = {pt_to_ml} ml")

    tbsp_to_ml = converter.convert(1, "tbsp", "ml")
    print(f"1 tbsp = {tbsp_to_ml} ml")

    tsp_to_ml = converter.convert(1, "tsp", "ml")
    print(f"1 tsp = {tbsp_to_ml} ml")

    cc_to_ml = converter.convert(1, "cc", "ml")
    print(f"1 cc = {cc_to_ml} ml")

    dl_to_ml = converter.convert(1, "dl", "ml")
    print(f"1 dl = {dl_to_ml} ml")

    kl_to_m3 = converter.convert(1, "kl", "m3")
    print(f"1 kl = {kl_to_m3} m³")

    hm3_to_m3 = converter.convert(1, "hm3", "m3")
    print(f"1 hm³ = {hm3_to_m3} m³")

    acft_to_m3 = converter.convert(1, "acft", "m3")
    print(f"1 acft = {acft_to_m3} m³")

    mcf_to_m3 = converter.convert(1, "mcf", "m3")
    print(f"1 mcf = {mcf_to_m3} m³")

    custom_value = converter.convert(2.5, "gal", "m3")
    print(f"2.5 gal = {custom_value} m³")

    reverse_conversion = converter.convert(liters_to_ml, "ml", "L")
    print(f"{liters_to_ml} ml = {reverse_conversion} L")

    large_volume = converter.convert(1000, "m3", "gal")
    print(f"1000 m³ = {large_volume} gal")

    small_volume = converter.convert(0.001, "m3", "ml")
    print(f"0.001 m³ = {small_volume} ml")

    chain_conversion = converter.convert(
        converter.convert(1, "gal", "L"), "L", "ml"
    )
    print(f"1 gal via L = {chain_conversion} ml")

    direct_conversion = converter.convert(1, "gal", "ml")
    print(f"1 gal direct = {direct_conversion} ml")

    ratio_check = abs(chain_conversion - direct_conversion)
    print(f"Chain vs direct difference: {ratio_check}")

    supported = converter.get_supported_units()
    print(f"Supported units count: {len(supported)}")

    converter.register_unit("liter", 1e-3)
    liter_to_ml = converter.convert(1, "liter", "ml")
    print(f"1 liter = {liter_to_ml} ml")

    converter.remove_unit("liter")
    try:
        converter.convert(1, "liter", "ml")
    except ValueError as e:
        print(f"Expected error after removal: {type(e).__name__}")

    invalid_unit_error = None
    try:
        converter.convert(1, "gallon", "L")
    except ValueError as e:
        invalid_unit_error = True
    print(f"Handled invalid unit error: {invalid_unit_error}")

if __name__ == '__main__':
    demonstrate_converter()