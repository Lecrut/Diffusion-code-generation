from decimal import Decimal, getcontext

getcontext().prec = 50

class VolumeMeasurement:
    def __init__(self, value, unit):
        if not isinstance(value, (int, float, Decimal)):
            raise TypeError("Value must be numeric")
        self.value = Decimal(str(value))
        self.unit = unit.lower()
        self._validate_unit()
        self._ensure_valid_unit_for_conversion()

    def _validate_unit(self):
        valid_units = {"cubic centimeters", "cc", "cm3", "liters", "l", "milliliters", "ml", "gallons", "gal", "cubic meters", "m3"}
        if self.unit not in valid_units:
            raise ValueError(f"Invalid unit: {self.unit}")

    def _ensure_valid_unit_for_conversion(self):
        self.value = self._to_cubic_centimeters(self.value, self.unit)

    @property
    def value_in_cm3(self):
        return self._to_cubic_centimeters(self.value, self.unit)

    def _to_cubic_centimeters(self, val, unit):
        conversions = {
            "cubic centimeters": Decimal("1"),
            "cc": Decimal("1"),
            "cm3": Decimal("1"),
            "liters": Decimal("1000"),
            "l": Decimal("1000"),
            "milliliters": Decimal("1"),
            "ml": Decimal("1"),
            "gallons": Decimal("3785.411784"),
            "gal": Decimal("3785.411784"),
            "cubic meters": Decimal("1000000"),
            "m3": Decimal("1000000"),
        }
        return val * conversions[unit]

    def convert_to(self, target_unit):
        if target_unit == self.unit:
            return Decimal(str(self.value))
        
        if target_unit.lower() in {"cubic centimeters", "cc", "cm3", "milliliters", "ml"}:
            val_cm3 = self._to_cubic_centimeters(self.value, self.unit)
            return val_cm3

        val_cm3 = self._to_cubic_centimeters(self.value, self.unit)
        
        conversions = {
            "cubic centimeters": Decimal("1"),
            "cc": Decimal("1"),
            "cm3": Decimal("1"),
            "milliliters": Decimal("1"),
            "ml": Decimal("1"),
            "liters": Decimal("0.001"),
            "l": Decimal("0.001"),
            "gallons": Decimal("0.000264172052"),
            "gal": Decimal("0.000264172052"),
            "cubic meters": Decimal("0.000001"),
            "m3": Decimal("0.000001"),
        }
        
        factor = conversions.get(target_unit.lower())
        if factor is None:
            raise ValueError(f"Target unit {target_unit} not supported")
            
        return val_cm3 * factor

    def add(self, other):
        if not isinstance(other, VolumeMeasurement):
            raise TypeError("Can only add VolumeMeasurement")
        val_cm3 = self._to_cubic_centimeters(self.value, self.unit) + self._to_cubic_centimeters(other.value, other.unit)
        return VolumeMeasurement(val_cm3, "cubic centimeters")

    def subtract(self, other):
        if not isinstance(other, VolumeMeasurement):
            raise TypeError("Can only subtract VolumeMeasurement")
        val_cm3 = self._to_cubic_centimeters(self.value, self.unit) - self._to_cubic_centimeters(other.value, other.unit)
        return VolumeMeasurement(val_cm3, "cubic centimeters")

    def __repr__(self):
        return f"VolumeMeasurement({self.value}, '{self.unit}')"

if __name__ == '__main__':
    vol1 = VolumeMeasurement(1.5, "liters")
    vol2 = VolumeMeasurement(500, "milliliters")
    vol3 = vol1.add(vol2)
    
    print(vol3.convert_to("gallons"))
    
    vol4 = VolumeMeasurement(1, "cubic meters")
    print(vol4.convert_to("liters"))
    
    vol5 = VolumeMeasurement(10, "gallons")
    print(vol5.convert_to("cubic centimeters"))