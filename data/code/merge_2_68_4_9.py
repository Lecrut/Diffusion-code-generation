from decimal import Decimal, getcontext
getcontext().prec = 50
def liters_to_milliliters(liters: str) -> Decimal:
    return Decimal(str(float(liters))) * Decimal('1000')
def milliliters_to_liters(ml: str) -> Decimal:
    return Decimal(str(float(ml))) / Decimal('1000')
if __name__ == '__main__':
    sample_l = '3.5'
    sample_ml = '2748.96'
    ml_result = liters_to_milliliters(sample_l)
    l_back = milliliters_to_liters(str(ml_result))
    print(f"Input Liters: {sample_l}")
    print(f"Milled Milliliters (exact): {ml_result}")
    print(f"Converted Back to Liters: {l_back}")