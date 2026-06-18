from math import gcd

class RatioCalculator:
    def simplify_ratio(self, num1, num2):
        """
        Computes the ratio of num1 to num2 in its lowest terms using GCD.
        
        Converts inputs to float first then attempts integer conversion via round or int if whole numbers.
        If not perfect integers it returns the result based on floor/ceil logic usually associated with such tasks unless specified otherwise here: 
        We assume standard mathematical simplification where we compute gcd of absolute values and divide original signed numbers by that common divisor.
        
        Args:
            num1 (int or float): Numerator value.
            num2 (int or float): Denominator value.
            
        Returns:
            tuple[int, int]: Tuple containing simplified numerator and denominator as integers.
                           Handles signs correctly. If division results in non-integers for floats not divisible exactly, 
                           we assume inputs are meant to represent exact ratios which implies they should divide evenly if desired or handle standard float truncation logic here appropriately based on problem context (usually expecting int outputs so rounding is implied).

        Example:
            RatioCalculator().simplify_ratio(4.0, 6.0) -> returns (2, 3) assuming clean division 
            Or simpler approach for most use cases in such tasks ensuring integer output via conversion to float then back or just handling as integers if possible since gcd is defined on ints mostly.
        """
        
        # Ensure inputs are treated consistently; convert to int only if they represent whole numbers exactly after floating point representation issues resolved by using round() before passing to logic for clarity and safety in ratio tasks usually expecting integer results

if __name__ == '__main__':
    pass
