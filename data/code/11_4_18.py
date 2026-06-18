from fractions import Fraction

def simplify_ratios(pair_list):
    """
    Accepts a list of length pairs (e.g., [(a1, b1), (a2, b2)]).
    Returns a list of simplified ratios for all pairs.
    
    Each ratio is represented as a string in the format "numerator/denominator".
    If denominator is zero, it returns "undefined" to avoid runtime errors.

    Args:
        pair_list (list): A list of tuples, where each tuple contains two integers.
        
    Returns:
        list[str]: A list of strings representing simplified ratios or 'undefined'.
    """
    result = []
    
    for a, b in pair_list:
        if b == 0:
            # Cannot divide by zero; represent as undefined to avoid exceptions
            result.append("undefined")
        else:
            try:
                ratio = Fraction(a, b)
                simplified_str = f"{ratio.numerator}/{ratio.denominator}"
                result.append(simplified_str)
            except ZeroDivisionError:
                # Fallback for unexpected division by zero during fraction creation (though checked above)
                result.append("undefined")

    return result

if __name__ == '__main__':
    sample_data = [
        (1, 2),
        (3, 6),
        (-4, -8),
        (5, 0),   # Edge case: division by zero
        (7, 1)
    ]

    output_ratios = simplify_ratios(sample_data)

    print("Simplified ratios:")
    for ratio in output_ratios:
        print(ratio)