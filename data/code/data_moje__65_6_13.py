from decimal import Decimal, getcontext

getcontext().prec = 50

FEET_TO_INCHES_RATIO = Decimal('12')

class FootConverter:
    def __init__(self):
        self.ratio = FEET_TO_INCHES_RATIO

    def convert(self, feet: float) -> float:
        feet_decimal = Decimal(str(feet))
        inches_decimal = feet_decimal * self.ratio
        return float(inches_decimal)

    def get_ratio(self) -> str:
        return str(self.ratio)

if __name__ == '__main__':
    converter = FootConverter()
    ratio = converter.get_ratio()
    print(f"Ratio: {ratio}")
    print(converter.convert(1.0))
    print(converter.convert(0.125))
    print(converter.convert(9.87654321))