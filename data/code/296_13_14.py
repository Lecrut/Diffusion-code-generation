class RatioHandler:
    @staticmethod
    def simplify(numerator, denominator):
        gcd = math.gcd(numerator, denominator)
        return numerator // gcd, denominator // gcd

    @classmethod
    def calculate_new_denominator(cls, numerator, denominator, target_numerator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        ratio = numerator / denominator
        new_denominator = (target_numerator * denominator) / numerator
        return int(round(new_denominator)) if abs(new_denominator - round(new_denominator)) < 1e-9 else new_denominator

if __name__ == '__main__':
    numerator = 3
    denominator = 4
    target_numerator = 15
    simplified_ratio = RatioHandler.simplify(numerator, denominator)
    new_denominator = RatioHandler.calculate_new_denominator(numerator, denominator, target_numerator)
    print(f"Simplified Ratio: {simplified_ratio}")
    print(f"New Denominator for Target Numerator: {new_denominator}")