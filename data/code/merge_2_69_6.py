import enum
from decimal import Decimal, getcontext
getcontext().prec = 50
class MassUnit(enum.Enum):
    KILOGRAM = "kg"
    GRAM = "g"
    POUND_MASS = "lbm"
    OUNCE_AVOIRPOIS = "oz"
    TON_SHORT = "ton"
    @classmethod
    def get_conversion_factor_to_kilogram(cls, unit: 'MassUnit') -> Decimal:
        factors = {
            MassUnit.KILOGRAM: Decimal("1"),
            MassUnit.GRAM: Decimal("0.001"),
            MassUnit.POUND_MASS: Decimal("0.45359237"),
            MassUnit.OUNCE_AVOIRPOIS: Decimal("0.028349523125"),
            MassUnit.TON_SHORT: Decimal("1000"),
        }
        return factors[unit]
def convert_mass(value: float, from_unit: MassUnit, to_unit: MassUnit) -> str:
    factor_from = MassUnit.get_conversion_factor_to_kilogram(from_unit)
    value_in_kg = Decimal(str(value)) * factor_from
    factor_to = MassUnit.get_conversion_factor_to_kilogram(to_unit)
    result_decimal = (value_in_kg / factor_to).quantize(Decimal("0.0001"))
    return f"{result_decimal} {to_unit.value}"
if __name__ == '__main__':
    sample_masses = [5, 2.5, 10]
    conversions = []
    for mass in sample_masses:
        result_kg = convert_mass(mass, MassUnit.KILOGRAM, MassUnit.GRAM)
        result_lb = convert_mass(mass, MassUnit.POUND_MASS, MassUnit.TON_SHORT)
        print(f"Input: {mass} kg")
        print(result_kg)
        print(result_lb)
        print("-" * 20)