class RatioConverter:
    def simplify(self, ratio_a, ratio_b):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        common_divisor = gcd(ratio_a, ratio_b)
        simplified_ratio_a = ratio_a // common_divisor
        simplified_ratio_b = ratio_b // common_divisor
        return (simplified_ratio_a, simplified_ratio_b)

if __name__ == '__main__':
    converter = RatioConverter()
    result = converter.simplify(180, 45)
    print(result)