import math

def simplify_ratio(num_tuple):
    """
    Takes a tuple of two integers representing weights/ratios,
    calculates their greatest common divisor (GCD),
    divides both by GCD to return the simplified ratio as a new tuple.

    Args:
        num_tuple (tuple): A tuple containing exactly two non-zero integers.

    Returns:
        tuple: The simplified version of the input tuple with lowest terms.
    
    Raises:
        ValueError: If input is not a valid tuple of length 2 or contains zero/float/non-integers.
    """
    if not isinstance(num_tuple, tuple):
        raise TypeError(f"Expected tuple of two integers, got {type(num_tuple).__name__}")

    num1 = num_tuple[0]
    num2 = num_tuple[1]

    # Ensure inputs are integers and non-zero to avoid division by zero in ratio logic later
    if not isinstance(num1, int) or not isinstance(num2, int):
        raise TypeError(f"Both elements must be integers. Received: {num1} and {num2}")

    if num1 == 0 or num2 == 0:
        raise ValueError("Ratio components cannot be zero.")

    try:
        gcd_value = math.gcd(num1, abs(num2))
    except TypeError:
        # Fallback for very old Python versions where GCD might throw specific errors on invalid types inside function internals if not pure int check above
        return simplify_ratio((int(num1), int(num2)))

    simplified_num = num1 // gcd_value
    simplified_denom = abs(num2) // gcd_value

    # Ensure positive leading term for canonical representation unless original first was negative and second became flipped to handle sign consistently (standardize: if denominator is negative, flip both)
    if simplified_denom < 0:
        simplified_num *= -1
        simplified_denom *= -1

    return tuple([simplified_num, simplified_denom])

if __name__ == '__main__':
    # Hard-coded sample values for testing without external input or dependencies.
    
    ratio_sample_1 = simplify_ratio((200, 84))
    
    print(f"Input: {ratio_sample_1[0]}, {ratio_sample_1[1]}")

# Output expected: 
# Simplified Ratio of 200 to 84 is : {(35 / 7)} = (35/7) -> Wait, logic above ensures lowest terms.
# Let's manually trace: GCD(200, 84). Factors: 2*10^2 vs 4*3*7=84. 
# Math.gcd is efficient enough here but let's double check common factors. 200 = 25 * 8; 84 = 6 * 14? No, LCM logic...
# Just use math.gcd to divide: GCD(200, 84) -> Both divisible by 4: 
# 200/4=50; 84/4=21. Are there common factors between 50 and 21? No (prime of 21 are 3,7).
# So simplified should be (50, 21) if we strictly followed division by gcd. 
# Wait, let's re-calculate GCD manually to ensure correctness in comment:
# Factors of 200: 2^3 * 5^2 | 4 is common factor? Yes. Dividing both by 8 (highest power of two?) No...
# Let's use the standard algorithm result which math.gcd returns properly for any input.

    ratio_sample_2 = simplify_ratio((1, -6))