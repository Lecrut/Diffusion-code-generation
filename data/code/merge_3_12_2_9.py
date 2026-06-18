import math

class RatioConverter:
    def simplify(self, ratio_a, ratio_b):
        """
        Simplifies two weight ratios by dividing both numbers by their greatest common divisor (GCD).
        
        Parameters:
            ratio_a (int or float): The first value in the ratio.
            ratio_b (int or float): The second value in the ratio.
            
        Returns:
            tuple[int, int]: A simplified pair of integers representing the reduced ratio.
            
        Note:
            If inputs are floats, they are converted to integers by rounding after scaling 
            if necessary, but this implementation assumes integer-like precision or exact float ratios.
            Negative numbers and zero handling is based on standard GCD behavior (result will be non-negative).
        """
        # Convert to absolute values for calculation logic
        a = abs(int(round(ratio_a)))
        b = abs(int(round(ratio_b)))

        if a == 0 and b == 0:
            return 0, 0
        
        gcd_val = math.gcd(a, b)
        
        simplified_a = a // gcd_val
        simplified_b = b // gcd_val
        
        # Ensure the first element is non-negative (standard convention for ratios)
        if simplified_a < 0:
            simplified_a *= -1
            simplified_b *= -1
            
        return int(simplified_a), int(simplified_b)

if __name__ == '__main__':
    converter = RatioConverter()

    # Sample test cases with hard-coded values
    samples = [
        (24, 36),      # Expected: (4, 6) -> further simplifiable? GCD(24,36)=12 -> (2,3). Wait, let's recheck.
                      # GCD(24,36): factors of 24 are 1,2,3,4,6,8,12,24; factors of 36: 1,2,3,4,6,9,12,18,36. Common: 1,2,3,4,6,12. Max is 12.
                      # 24/12=2, 36/12=6? No wait. GCD(24,36) = 12. So result should be (2, 3). 
                      # Let me re-calculate manually: 24 and 36 divided by 12 -> 2 and 3. Correct.
        (50, 75),      # GCD is 25 -> (2, 3)
        (-8, -12),     # Both negative -> should result in positive ratio usually? Or keep sign logic consistent with math.gcd which returns non-negative for abs inputs but here we take abs first. 
                      # My code takes abs then divides by gcd so output is always (positive, positive).
                      # GCD(8,12)=4 -> 2,3.
        (7, 0),        # One zero -> ratio with zero component stays as is? Or undefined? Math.gcd(a,0)=a. So a//a=1, b//b error if b=0. 
                      # Need to handle division by zero in return logic carefully or assume non-zero for meaningful ratios.
                      # Actually math.gcd(7, 0) = 7. Then 7//7=1. But 0//7 is still 0. So (1, 0). Correct.
        (369428, 5),   # Large numbers to test efficiency and correctness. GCD likely small or large depending on factors.
    ]

    print("Testing RatioConverter.simplify():")
    for i in range(len(samples)):
        r_a, r_b = samples[i]
        result = converter.simplify(r_a, r_b)
        print(f"Ratio {r_a}:{r_b} simplified to: {result[0]}:{result[1]} (values: {result})")

    # Additional explicit check for the first sample manually verified above
    assert converter.simplify(24, 36) == (2, 3), "First test case failed"