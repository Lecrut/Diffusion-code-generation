from decimal import Decimal, getcontext

getcontext().prec = 50

def compute_cone_volume(radius: Decimal, height: Decimal) -> Decimal:
    pi = Decimal("3.14159265358979323846264338327950288419716939937510")
    return (pi * radius * radius * height) / Decimal(3)

if __name__ == "__main__":
    radius = Decimal("2.5")
    height = Decimal("4.0")
    volume = compute_cone_volume(radius, height)
    print(volume)