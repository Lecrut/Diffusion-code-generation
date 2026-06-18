import math
from functools import reduce
from operator import mul

def simplify_ratio(ratios):
    """
    Takes a list of weight ratios (as tuples of integers) and returns 
    a new list with each ratio simplified to its lowest terms.
    
    A ratio is represented as an iterable of two integers [a, b].
    The function computes the greatest common divisor (GCD) for each pair 
    and divides both numbers by this GCD. If any part of the input list 
    is not a sequence of exactly two elements, that item will be skipped 
    to avoid runtime errors in an interactive environment where unexpected data types are possible.
    
    Args:
        ratios (list): A list containing tuples or lists of length 2 representing numerators and denominators.
        
    Returns:
        list: A list of simplified integer pairs [[a1, b1], [a2, b2], ...].
             If the input contains negative numbers, they are handled such that 
             only the sign is preserved on the numerator if possible (e.g., (-4, 6) -> (-2, 3)).
    """
    
    def gcd(a, b):
        a = abs(a)
        b = abs(b)
        while b:
            a, b = b, a % b
        return a
    
    simplified_list = []
    
    for ratio in ratios:
        if isinstance(ratio, (list, tuple)) and len(ratio) == 2:
            try:
                val1 = int(ratio[0])
                val2 = int(ratio[1])
                
                common_divisor = gcd(val1, val2)
                
                simplified_val1 = val1 // common_divisor
                simplified_val2 = val2 // common_divisor
                
                # Ensure the denominator is positive; if it's negative and numerator isn't, flip signs to keep standard form.
                if simplified_val2 < 0:
                    simplified_val1 *= -1
                    simplified_val2 *= -1
                    
                simplified_list.append([simplified_val1, simplified_val2])
            except (ValueError, TypeError):
                # Skip non-integer or invalid inputs within the list to maintain robustness for potential edge cases.
                pass
                
    return simplified_list

if __name__ == '__main__':
    # Hard-coded sample values as requested: a list of weight ratios [[a1,b1], [a2,b2]] etc.
    input_ratios = [['4', '6'], ['8', 10], [-3, 9], [5, -10], [7, 7]]

    # Convert string numbers in the first entry to integers for processing if necessary
    processed_input = [[int(x) for x in r] if isinstance(r[0], str) else list(map(int, r)) for r in input_ratios]

    result = simplify_ratio(processed_input)

    print(f"Input Ratios: {processed_input}")
    print(f"Simplified Ratios: {result}")