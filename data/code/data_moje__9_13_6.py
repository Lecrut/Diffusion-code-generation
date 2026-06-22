from decimal import Decimal, getcontext

getcontext().prec = 10

_ML_TO_L = Decimal('0.001')
_M3_TO_L = Decimal('1000')
_GAL_TO_L = Decimal('3.785411784')
_L_TO_ML = Decimal('1000')
_L_TO_M3 = Decimal('0.001')
_L_TO_GAL = Decimal('0.264172052')

def convert_milliliters_to_liters(value: Decimal) -> Decimal:
    return value * _ML_TO_L

def convert_liters_to_milliliters(value: Decimal) -> Decimal:
    return value * _L_TO_ML

def convert_cubic_meters_to_liters(value: Decimal) -> Decimal:
    return value * _M3_TO_L

def convert_liters_to_cubic_meters(value: Decimal) -> Decimal:
    return value * _L_TO_M3

def convert_gallons_to_liters(value: Decimal) -> Decimal:
    return value * _GAL_TO_L

def convert_liters_to_gallons(value: Decimal) -> Decimal:
    return value * _L_TO_GAL

def convert_metric_to_imperial(liters: Decimal) -> tuple:
    ml = convert_liters_to_milliliters(liters)
    gal = convert_liters_to_gallons(liters)
    return ml, gal

def convert_imperial_to_metric(gallons: Decimal, milliliters: Decimal) -> tuple:
    l_from_gal = convert_gallons_to_liters(gallons)
    l_from_ml = convert_milliliters_to_liters(milliliters)
    total_liters = l_from_gal + l_from_ml
    cubic_meters = convert_liters_to_cubic_meters(total_liters)
    return total_liters, cubic_meters

if __name__ == '__main__':
    val_liters = Decimal('5.5')
    val_milliliters = convert_liters_to_milliliters(val_liters)
    print(val_milliliters)

    val_gallons = Decimal('2.0')
    val_liters_from_gal = convert_gallons_to_liters(val_gallons)
    print(val_liters_from_gal)

    val_m3 = Decimal('1.5')
    val_liters_from_m3 = convert_cubic_meters_to_liters(val_m3)
    print(val_liters_from_m3)

    result = convert_metric_to_imperial(val_liters)
    print(result)

    result2 = convert_imperial_to_metric(val_gallons, val_milliliters)
    print(result2)