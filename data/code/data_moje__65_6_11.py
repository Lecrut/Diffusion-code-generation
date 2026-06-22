from decimal import Decimal
from typing import Union

def feet_to_inches(feet: float) -> float:
    dec_feet = Decimal(str(feet))
    dec_inches = dec_feet * Decimal('12')
    return float(dec_inches)

if __name__ == '__main__':
    sample_feet = 5.25
    result = feet_to_inches(sample_feet)
    print(result)