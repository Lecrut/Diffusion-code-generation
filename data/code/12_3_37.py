from math import gcd

def simplify_ratios(weight_ratios):
    def parse_ratio(ratio):
        try:
            numerator, denominator = map(int, ratio.split(':'))
            if denominator == 0:
                raise ValueError("Denominator cannot be zero.")
            return numerator, denominator
        except ValueError as e:
            raise ValueError(f"Invalid ratio '{ratio}': {e}")

    def simplify_ratio(numerator, denominator):
        common_divisor = gcd(numerator, denominator)
        return f"{numerator // common_divisor}:{denominator // common_divisor}"

    simplified_ratios = []
    for ratio in weight_ratios:
        numerator, denominator = parse_ratio(ratio)
        simplified_ratios.append(simplify_ratio(numerator, denominator))
    
    return simplified_ratios

if __name__ == '__main__':
    sample_ratios = ["6:8", "15:20", "9:3", "7:4"]
    print(simplify_ratios(sample_ratios))