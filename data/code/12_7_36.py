from math import gcd

class RatioSimplifier:
    def __init__(self, ratio_dict):
        self.ratio_dict = ratio_dict

    def simplify(self):
        simplified_dict = {}
        for name, ratio in self.ratio_dict.items():
            num, denom = map(int, ratio.split(':'))
            common_divisor = gcd(num, denom)
            simplified_ratio = f"{num // common_divisor}:{denom // common_divisor}"
            simplified_dict[name] = simplified_ratio
        return simplified_dict

if __name__ == '__main__':
    sample_ratios = {
        'ratio1': '4:8',
        'ratio2': '10:25',
        'ratio3': '7:21'
    }
    simplifier = RatioSimplifier(sample_ratios)
    print(simplifier.simplify())