from decimal import Decimal, getcontext
getcontext().prec = 50
def liters_to_milliliters(liters: str) -> str:
    d_liters = Decimal(liters)
    return str(d_liters * Decimal('1000'))
def milliliters_to_literes(ml: str) -> str:
    d_ml = Decimal(ml)
    return str(d_ml / Decimal('1000'))
if __name__ == '__main__':
    sample_liters = "2.5"
    sample_milliliters = "374968.2"
    result_l_to_ml = liters_to_milliliters(sample_liters)
    print(f"{sample_liters} L -> {result_l_to_ml} mL")
    result_ml_to_L = milliliters_to_literes(sample_milliliters)
    print(f"{sample_milliliters} mL -> {result_ml_to_L} L")