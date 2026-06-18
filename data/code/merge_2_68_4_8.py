from decimal import Decimal, getcontext
getcontext().prec = 50
def liters_to_milliliters(liters: str) -> int:
    d_liters = Decimal(liters) * Decimal('1000')
    return int(d_liters.to_integral_value(rounding='ROUND_HALF_UP'))
def milliliters_to_liter(ml: str) -> float:
    d_ml = Decimal(ml) / Decimal('1000')
    return float(d_ml.to_integral_value(rounding='ROUND_HALF_UP'))
if __name__ == '__main__':
    test_liters_values = ['1.5', '2.34567890123456789012345678901234567890']
    test_ml_values = ['1500', '2345678.90123456789012345678901234567890']
    print("Liters to Milliliters Conversion:")
    for val in test_liters_values:
        result = liters_to_milliliters(val)
        print(f"{val} L -> {result} mL")
    print("\nMilliliters to Liters Conversion:")
    for val in test_ml_values:
        result = milliliters_to_liter(val)
        print(f"{val} mL -> {result:.15f} L")