from math import gcd
from typing import Dict

def simplify_ratios(ratios: Dict[str, tuple]) -> Dict[str, tuple]:
    simplified_ratios = {}
    for name, (numerator, denominator) in ratios.items():
        common_divisor = gcd(numerator, denominator)
        simplified_numerator = numerator // common_divisor
        simplified_denominator = denominator // common_divisor
        simplified_ratios[name] = (simplified_numerator, simplified_denominator)
    return simplified_ratios

if __name__ == '__main__':
    sample_ratios = {
        'ratio1': (8, 12),
        'ratio2': (100, 400),
        'ratio3': (7, 9),
        'ratio4': (25, 15)
    }
    simplified = simplify_ratios(sample_ratios)
    print(simplified)