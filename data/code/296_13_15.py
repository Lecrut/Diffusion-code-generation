class RatioHandler:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    @staticmethod
    def simplify_ratio(numerator, denominator):
        gcd = math.gcd(numerator, denominator)
        return (numerator // gcd, denominator // gcd)

    def calculate_new_denominator(self, target_numerator):
        if self.denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        ratio = self.numerator / self.denominator
        new_denominator = target_numerator / ratio
        if abs(new_denominator - round(new_denominator)) < 1e-9:
            return int(round(new_denominator))
        else:
            return new_denominator

if __name__ == '__main__':
    numerator = 3
    denominator = 4
    target_numerator = 15

    ratio_handler = RatioHandler(numerator, denominator)
    simplified_ratio = RatioHandler.simplify_ratio(numerator, denominator)
    new_denominator = ratio_handler.calculate_new_denominator(target_numerator)

    print(f"Original Ratio: {numerator}/{denominator}")
    print(f"Simplified Ratio: {simplified_ratio[0]}/{simplified_ratio[1]}")
    print(f"Target Numerator: {target_numerator}")
    print(f"New Denominator: {new_denominator}")