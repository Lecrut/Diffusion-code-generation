from decimal import Decimal, getcontext
getcontext().prec = 50
def liters_to_milliliters(liters: str) -> str:
    d_liters = Decimal(liters)
    return str(d_liters * Decimal('1000'))
def milliliters_to_literes(ml: str) -> str:
    d_ml = Decimal(ml)
    return str(d_ml / Decimal('1000'))
if __name__ == '__main__':
    sample_liters = '3.14159265358'
    sample_milliliters = '7500.000000000000000000'
    print(f"Input Liters: {sample_liters}")
    result_ml = liters_to_milliliters(sample_liters)
    print(f"Converted to Milliliters: {result_ml}")
    print(f"\nInput Milliliters: {sample_milliliters}")
    result_literes = milliliters_to_literes(sample_milliliters)
    print(f"Converted back to Liters: {result_literes}")