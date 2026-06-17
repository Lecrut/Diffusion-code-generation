import decimal
from decimal import Decimal, getcontext
getcontext().prec = 50
def convert_mass(value: str, from_unit: str, to_unit: str) -> tuple[Decimal, float]:
    conversion_factors = {
        "kg": Decimal("1"),
        "lb": Decimal("453.59237"),
        "g": Decimal("0.001"),
        "oz": Decimal("0.0625"),                     
    }
    def to_kilograms(value: Decimal, unit: str) -> Decimal:
        factor = conversion_factors.get(unit.lower(), None)
        if not factor or value == Decimal(0):
            return value
        return (value * factor).normalize()
    from_unit_lower = from_unit.lower().strip()
    to_unit_lower = to_unit.lower().strip()
    decimal_value = Decimal(value.strip())
    kg_value = to_kilograms(decimal_value, from_unit_lower)
    final_decimal = (kg_value / conversion_factors[to_unit_lower]).normalize()
    final_float = float(final_decimal)
    return final_decimal, final_float
if __name__ == '__main__':
    sample_input_mass = "10"
    sample_from_unit = "lb"
    sample_to_unit = "g"
    result_decimal, result_float = convert_mass(sample_input_mass, sample_from_unit, sample_to_unit)
    print(f"Input: {sample_input_mass} {sample_from_unit}")
    print(f"Output (Decimal): {result_decimal}")
    print(f"Output (Float): {result_float}")