from decimal import Decimal, getcontext
getcontext().prec = 50
def liters_to_milliliters(liters: str) -> str:
    d_liters = Decimal(liters)
    return str(d_liters * Decimal('1000'))
def milliliters_to_liter(ml: str) -> str:
    d_ml = Decimal(ml)
    return str(d_ml / Decimal('1000'))
if __name__ == '__main__':
    sample_liters = "0.003456789"
    sample_milliliters = "3456789.123456789"
    print(f"Liters: {sample_liters}")
    result_ml = liters_to_milliliters(sample_liters)
    print(f"Milliliters (from Liters): {result_ml}")
    print(f"\nMilliliters: {sample_milliliters}")
    result_liter = milliliters_to_liter(sample_milliliters)
    print(f"Liters (from Milliliters): {result_liter}")