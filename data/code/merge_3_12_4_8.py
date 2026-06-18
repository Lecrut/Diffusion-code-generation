import math
from fractions import Fraction

def simplify_ratios(ratios):
    """
    Takes a list of weight ratios (as lists/tuples or strings representing 'a:b')
    and returns a new list containing the simplified forms as tuples.
    
    A ratio is considered to be in its simplest form if:
    1. Both numbers are integers.
    2. They share no common divisor other than 1 (GCD).
    3. The first number is non-negative, and if zero, the second must also be positive or handled logically.

    Args:
        ratios (list): List of input ratio representations. Each element can be a list [a, b], 
                      tuple (a, b), string "a:b", or two separate integers passed as elements in sub-lists/tuples.
    
    Returns:
        list: A new list where each original ratio has been simplified to its lowest terms.

    Note: This function assumes valid integer inputs representing weights. Negative numbers are allowed 
            but the sign is normalized such that the first non-zero number determines the overall sign convention,
            typically ensuring the result starts with a positive number if possible for standard weight representation.
    """
    
    def get_gcd(a, b):
        return math.gcd(abs(int(a)), abs(int(b)))

    def normalize_sign(num1, num2):
        # Ensure that the first non-zero element is positive to maintain consistency in sign convention
        if num1 == 0:
            if num2 < 0:
                return -num1, -num2  # Both zero? Keep as is or handle logic. Assuming valid input here.
            else:
                return num1, num2
        elif num1 > 0 and num2 >= 0:
            pass
        elif num1 < 0 and num2 <= 0:
            if abs(num1) == abs(num2): # Both negative equal magnitude? 
                 return -num1, -num2 # Make both positive to simplify sign ambiguity in weights.
            else:
                # Normalize so that the first number is positive by flipping signs of both
                return num1 * (-1), num2 * (-1) if (num1 < 0 and num2 > 0 or num1 > 0 and num2 < 0) else None
        
        # If mixed sign, flip to make first one positive. 
        elif num1 < 0:
            return -num1, -num2
        else:
            return num1, num2

    def parse_ratio(r):
        if isinstance(r, (list, tuple)):
            a = r[0]
            b = r[1]
        elif isinstance(r, str) and ':' in r:
            parts = r.split(':')
            a = int(parts[0].strip())
            b = int(parts[1].strip())
        else:
            raise ValueError(f"Unsupported ratio format: {r}")

    def simplify(a, b):
        common_divisor = get_gcd(int(a), int(b))
        
        # Normalize signs first to ensure consistent output (first non-zero positive)
        a_norm, b_norm = normalize_sign(a, b)
        
        simplified_a = a_norm // common_divisor
        simplified_b = b_norm // common_divisor
        
        return tuple(simplified_a, simplified_b)

    result_list = []
    
    for ratio in ratios:
        try:
            parsed_ratio = parse_ratio(ratio)
            if not isinstance(parsed_ratio[0], int): 
                continue # Skip non-integer inputs gracefully or raise error depending on strictness. Assuming integers here.
            
            simplified_tuple = simplify(*parsed_ratio)
            result_list.append(simplified_tuple)
        except Exception:
            pass

    return result_list

if __name__ == '__main__':
    sample_ratios = [
        ["2", "4"],           # Input as strings in list format -> Output (1, 2)
        [(3, 6)],             # Input as tuple -> Output (1, 2)
        ["5:10"],             # Input as string with colon separator -> Output (1, 2)
        [4, 8],               # Direct integers in list -> Output (1, 2)
        [-3, -6],             # Negative inputs normalized to positive -> Output (1, 2)
        ["0", "5"],           # Zero first element -> Output (0, 1)
        [7, 49]               # Large common factor -> Output (1, 7)
    ]

    simplified_output = simplify_ratios(sample_ratios)

    print("Original Ratios:", sample_ratios)
    print("\nSimplified Ratios:")
    for i, original in enumerate(sample_ratios):
        print(f"Input: {original} -> Output: {simplified_output[i]}")