class RatioConverter:
    def __init__(self):
        pass
    
    @staticmethod
    def gcd(a, b):
        """Calculate the Greatest Common Divisor using Euclidean algorithm."""
        a = abs(a)
        b = abs(b)
        while b != 0:
            temp = b
            b = a % b
            a = temp
        return a
    
    def simplify(self, ratio_a, ratio_b):
        """Simplify the weight ratios by dividing both numbers by their GCD."""
        common_divisor = self.gcd(ratio_a, ratio_b)
        simplified_ratio_a = ratio_a // common_divisor
        simplified_ratio_b = ratio_b // common_divisor
        return (simplified_ratio_a, simplified_ratio_b)

if __name__ == '__main__':
    # Hard-coded sample values to test the RatioConverter class without user input
    converter = RatioConverter()

    # Test case 1: Simple integer ratios
    result_1 = converter.simplify(60, 45)
    print(f"Simplified ratio of {60}:{45} is {result_1}")

    # Test case 2: Negative integers (should work correctly with absolute GCD logic)
    result_2 = converter.simplify(-8, -12)
    print(f"Simplified ratio of {-8}:-{12} is {result_2}")

    # Test case 3: Larger numbers to test efficiency
    result_3 = converter.simplify(94608, 57750)
    print(f"Simplified ratio of {94608}:{57750} is {result_3}")

    # Expected output examples based on logic:
    # (12/15 -> divide by 3 -> 4/5) for case 1
    # (-2/-4 -> divide by -2 or treat as magnitudes depending on GCD implementation, here it divides signs out in magnitude usually but our gcd takes abs then we preserve sign of input? 
    # Actually my gcd returns positive. The division will keep the original signs if inputs were negative because // preserves sign logic relative to divisor which is always positive from gcd result
    # Wait: -8 / 4 = -2, -12 / 4 = -3. So (-2, -3). 
    # Case 3: GCD(94608, 57750) -> let's trace roughly or assume correct math applies.