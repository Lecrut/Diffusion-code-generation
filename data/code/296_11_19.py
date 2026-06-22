class RatioScaler:
    DEFAULT_FACTOR = 2

    @staticmethod
    def calculate_ratio(numerator, denominator):
        common_divisor = gcd(numerator, denominator)
        return (numerator // common_divisor, denominator // common_divisor)

    @classmethod
    def scale_and_format(cls, ratio, factor=DEFAULT_FACTOR):
        scaled_ratio = cls.calculate_ratio(ratio[0] * factor, ratio[1] * factor)
        return f"{scaled_ratio[0]}:{scaled_ratio[1]}"

if __name__ == '__main__':
    scaler = RatioScaler()
    sample1 = (6, 9)
    print(scaler.scale_and_format(sample1))
    sample2 = (10, 15)
    print(scaler.scale_and_format(sample2, factor=4))