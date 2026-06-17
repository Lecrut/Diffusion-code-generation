from decimal import Decimal, getcontext
getcontext().prec = 50
def liters_to_milliliters(liters: str) -> Decimal:
    return Decimal(liters) * Decimal('1000')
def milliliters_to_liters(milliliters: str) -> Decimal:
    return Decimal(milliliters) / Decimal('1000')
if __name__ == '__main__':
    sample_l = '2.5'
    sample_ml = '3748965.123456789'
    result_1 = liters_to_milliliters(sample_l)
    print(f"{sample_l} L -> {result_1} mL")
    result_2 = milliliters_to_liters(sample_ml)
    print(f"{sample_ml} mL -> {result_2} L")