import math

class RatioScaler:
    @staticmethod
    def scale_ratio(ratio, factor):
        num = ratio[0] * factor
        den = ratio[1] * factor
        common_divisor = math.gcd(num, den)
        new_num = num // common_divisor
        new_den = den // common_divisor
        return f"{new_num}:{new_den}"

if __name__ == '__main__':
    scaler = RatioScaler()
    result1 = scaler.scale_ratio((6, 9), 2)
    print(result1)
    result2 = scaler.scale_ratio((10, 15), 4)
    print(result2)