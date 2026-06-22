from decimal import Decimal, getcontext

def km_to_m(km: Decimal) -> Decimal:
    getcontext().prec = 28
    return km * Decimal("1000")

if __name__ == '__main__':
    sample_km = Decimal("1.234567890123456789012345678")
    result = km_to_m(sample_km)
    print(result)