from decimal import Decimal, getcontext
getcontext().prec = 50
def celsius_to_fahrenheit(c: float) -> str:
    d_c = Decimal(str(c)) * Decimal('9') / Decimal('5') + Decimal('32')
    return format(d_c, '.10f')
def fahrenheit_to_celsius(f: float) -> str:
    d_f = Decimal(str(f)) - Decimal('32')
    result = (d_f * Decimal('5')) / Decimal('9')
    return format(result, '.10f')
def celsius_to_kelvin(c: float) -> str:
    d_c = Decimal(str(c)) + Decimal('273.15')
    return format(d_c, '.10f')
def kelvin_to_celsius(k: float) -> str:
    d_k = Decimal(str(k)) - Decimal('273.15')
    return format(d_k, '.10f')
if __name__ == '__main__':
    print(celsius_to_fahrenheit(0.0))
    print(fahrenheit_to_celsius(32.0) + " (should be 0)")
    print(celsius_to_kelvin(-459.67))
    print(kelvin_to_celsius(273.15))