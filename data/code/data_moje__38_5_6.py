from decimal import Decimal, getcontext

getcontext().prec = 28

def compute_cone_volume(radius: float, height: float) -> Decimal:
    r = Decimal(str(radius))
    h = Decimal(str(height))
    pi = Decimal('3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679')
    return (Decimal(1) / Decimal(3)) * pi * r ** 2 * h

if __name__ == '__main__':
    result = compute_cone_volume(2.5, 4.0)
    print(result)