from decimal import Decimal, getcontext
getcontext().prec = 50
def liters_to_milliliters(liters: str) -> str:
    d_liters = Decimal(liters)
    conversion_factor = Decimal('1000')
    result = d_liters * conversion_factor
    return str(result.normalize())
def milliliters_to_liter(milliliters: str) -> str:
    d_mililiters = Decimal(milliliters)
    conversion_factor = Decimal('0.001')
    result = d_mililiters * conversion_factor
    return str(result.normalize())
if __name__ == '__main__':
    test_liters = "3.14159265358979"
    ml_result = liters_to_milliliters(test_liters)
    print(f"{test_liters} Litres = {ml_result} Millilitres")
    back_liters = milliliters_to_liter(ml_result)
    print(f"{ml_result} Millilitres = {back_liters} Litres")