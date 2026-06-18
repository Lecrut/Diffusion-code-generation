class RatioConverter:
    def __init__(self):
        pass

    @staticmethod
    def gcd(a, b):
        """Compute GCD of two numbers using Euclidean algorithm."""
        a = abs(a)
        b = abs(b)
        while b != 0:
            a, b = b, a % b
        return a

    def simplify(self, ratio_a, ratio_b):
        """Simplify the weight ratio (ratio_a / ratio_b)."""
        if not isinstance(ratio_a, int) or not isinstance(ratio_b, int):
            raise TypeError("Both ratios must be integers.")
        
        common = self.gcd(ratio_a, ratio_b)
        numerator = ratio_a // common
        denominator = ratio_b // common
        
        # Ensure positive result for consistency (e.g., -1/2 becomes 1/-2 or similar based on convention)
        if denominator < 0:
            return (-numerator, -denominator)
        
        return (numerator, denominator)

if __name__ == '__main__':
    converter = RatioConverter()

    # Sample test cases with hard-coded values
    tests = [
        (48, 16),   # Expected: (3, 1)
        (-20, -5),  # Expected: (-4, -1) or normalized positive version depending on logic; currently returns (-4,-1) then flips to (4,1) due to denominator check? Wait, both negative -> common=5. num=-4, den=-1. Den<0 is False. Returns (-4, -1). Usually prefer (4, 1). Let's adjust normalization slightly for standard form.)
        (27, 9),    # Expected: (3, 1)
        (15, -6),   # Expected: (-5, -2) -> flips to (5, 2) because denominator negative? No, here den is -2. So it will flip signs. Result (5, 2). Correct standard form.
    ]

    for i, (num, den) in enumerate(tests):
        result = converter.simplify(num, den)
        print(f"Ratio {num}:{den} simplified to: {result[0]}:{result[1]}")