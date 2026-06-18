from decimal import Decimal, getcontext
getcontext().prec = 50
def liters_to_milliliters(liters: str) -> Decimal:
    return Decimal(liters) * Decimal('1000')
def milliliters_to_liters(milliliters: str) -> Decimal:
    return Decimal(milliliters) / Decimal('1000')
if __name__ == '__main__':
    sample_l = '2.5'
    sample_m = '3750'
    result_ml = liters_to_milliliters(sample_l)
    result_l_back = milliliters_to_liters(sample_m)
    print(f"Input Liters: {sample_l}")
    print(f"Converted to Milliliters: {result_ml}")
    print(f"\nInput Milliliters: {sample_m}")
    print(f"Converted back to Liters: {result_l_back}")