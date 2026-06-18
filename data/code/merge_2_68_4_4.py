from decimal import Decimal, getcontext
getcontext().prec = 50
def liters_to_milliliters(liters: str) -> Decimal:
    return Decimal(liters) * Decimal('1000')
def milliliters_to_liters(milliliters: str) -> Decimal:
    return Decimal(milliliters) / Decimal('1000')
if __name__ == '__main__':
    sample_l = '2.5'
    sample_ml = '374896'
    ml_result = liters_to_milliliters(sample_l)
    l_back = milliliters_to_liters(str(ml_result))
    print(f"Input Liters: {sample_l}")
    print(f"Milled Result: {ml_result}")
    print(f"Back to Liters: {l_back}")