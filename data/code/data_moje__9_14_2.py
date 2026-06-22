class VolumeConverter:
    LITER_TO_ML = 1000.0
    GALLON_TO_LITER = 3.785411784
    QUART_TO_GALLON = 0.25
    PINT_TO_QUART = 0.5
    CUP_TO_PINT = 0.5
    FL_OZ_TO_CUP = 0.125

    def __init__(self):
        self._ml = 0.0

    def _to_ml(self, value, unit):
        if unit == 'ml':
            return value
        if unit == 'L':
            return value * self.LITER_TO_ML
        if unit == 'gal':
            return value * self.GALLON_TO_LITER * self.LITER_TO_ML
        if unit == 'qt':
            return value * self.GALLON_TO_LITER * self.LITER_TO_ML * self.QUART_TO_GALLON
        if unit == 'pt':
            return value * self.GALLON_TO_LITER * self.LITER_TO_ML * self.QUART_TO_GALLON * self.PINT_TO_QUART
        if unit == 'cup':
            return value * self.GALLON_TO_LITER * self.LITER_TO_ML * self.QUART_TO_GALLON * self.PINT_TO_QUART * self.CUP_TO_PINT
        if unit == 'fl_oz':
            return value * self.GALLON_TO_LITER * self.LITER_TO_ML * self.QUART_TO_GALLON * self.PINT_TO_QUART * self.CUP_TO_PINT * self.FL_OZ_TO_CUP
        raise ValueError(f"Unknown unit: {unit}")

    def convert(self, value, from_unit, to_unit):
        ml_value = self._to_ml(value, from_unit)
        if to_unit == 'ml':
            return ml_value
        if to_unit == 'L':
            return ml_value / self.LITER_TO_ML
        if to_unit == 'gal':
            return ml_value / (self.GALLON_TO_LITER * self.LITER_TO_ML)
        if to_unit == 'qt':
            return ml_value / (self.GALLON_TO_LITER * self.LITER_TO_ML * self.QUART_TO_GALLON)
        if to_unit == 'pt':
            return ml_value / (self.GALLON_TO_LITER * self.LITER_TO_ML * self.QUART_TO_GALLON * self.PINT_TO_QUART)
        if to_unit == 'cup':
            return ml_value / (self.GALLON_TO_LITER * self.LITER_TO_ML * self.QUART_TO_GALLON * self.PINT_TO_QUART * self.CUP_TO_PINT)
        if to_unit == 'fl_oz':
            return ml_value / (self.GALLON_TO_LITER * self.LITER_TO_ML * self.QUART_TO_GALLON * self.PINT_TO_QUART * self.CUP_TO_PINT * self.FL_OZ_TO_CUP)
        raise ValueError(f"Unknown target unit: {to_unit}")

    def set_ml(self, value):
        self._ml = value
        return self

    def get_ml(self):
        return self._ml

    def get_L(self):
        return self._ml / self.LITER_TO_ML

    def get_gal(self):
        return self._ml / (self.GALLON_TO_LITER * self.LITER_TO_ML)

    def get_qt(self):
        return self._ml / (self.GALLON_TO_LITER * self.LITER_TO_ML * self.QUART_TO_GALLON)

    def get_pt(self):
        return self._ml / (self.GALLON_TO_LITER * self.LITER_TO_ML * self.QUART_TO_GALLON * self.PINT_TO_QUART)

    def get_cup(self):
        return self._ml / (self.GALLON_TO_LITER * self.LITER_TO_ML * self.QUART_TO_GALLON * self.PINT_TO_QUART * self.CUP_TO_PINT)

    def get_fl_oz(self):
        return self._ml / (self.GALLON_TO_LITER * self.LITER_TO_ML * self.QUART_TO_GALLON * self.PINT_TO_QUART * self.CUP_TO_PINT * self.FL_OZ_TO_CUP)

if __name__ == '__main__':
    converter = VolumeConverter()
    print(converter.convert(1, 'L', 'ml'))
    print(converter.convert(1, 'gal', 'L'))
    print(converter.convert(32, 'fl_oz', 'cup'))
    print(converter.set_ml(5000).get_gal())