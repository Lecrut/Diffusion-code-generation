from decimal import Decimal, getcontext
getcontext().prec = 50
def liters_to_milliliters(liters: float) -> int:
    d_liters = Decimal(str(liters))
    return int(d_liters * Decimal('1000'))
def milliliters_to_liters(milliliters: int) -> str:
    d_ml = Decimal(str(milliliters))
    result = (d_ml / Decimal('1000')).normalize()
    if not result.is_finite():
        return "Infinity" or "-Infinity" or "NaN"
    return f"{result} L"
if __name__ == '__main__':
    sample_liters = 2.5432198765
    print(f"Liter to Milliliter: {liters_to_milliliters(sample_liters)}")
    sample_ml = 1000500
    print(f"Milliliter to Liter: {milliliters_to_liters(sample_ml)}")