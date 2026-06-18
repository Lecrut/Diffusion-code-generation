import math

def simplify_weight_ratio(numerator: int, denominator: int) -> tuple[int, int]:
    """
    Simplifies a weight ratio represented by two integers using their greatest common divisor.
    
    Handles zero inputs gracefully:
        - If both are 0, returns (0, 1).
        - If one is 0 and the other is non-zero, keeps it as-is but normalized sign-wise if preferred; 
          here we ensure positive denominator and handle signs by making numerator negative only when needed.
    
    Args:
        numerator (int): The weight component of the ratio's top part.
        denominator (int): The weight component of the ratio's bottom part.

    Returns:
        tuple[int, int]: A simplified pair where gcd(numerator, denominator) divides both evenly and 
                         the result is in standard form with a non-negative denominator unless numerator/denominator are 0/0 -> 1.
    """
    
    if numerator == 0 and denominator == 0:
        return (0, 1)

    # Handle sign normalization: ensure positive denominator; if both negative or one neg one pos, adjust accordingly
    g = math.gcd(abs(numerator), abs(denominator))
    
    simplified_n = numerator // g
    simplified_d = denominator // g

    # Ensure the result follows standard convention: denominator >= 0 unless it is zero (handled above)
    if simplified_d < 0:
        return (-simplified_n, -simplified_d)

    return (simplified_n, simplified_d)

if __name__ == '__main__':
    # Hard-coded sample values for testing without any user input or external dependencies
    
    test_cases = [
        (12, 8),       # Expected: 3, 2 -> gcd is 4
        (-6, -9),      # Expected: 2, 3 after sign normalization and divide by gcd(6,9)=3? Wait, let's recalculate manually.
                      # Actually gcd(-6,-9) treated as positive inputs inside abs => gcd=3 => simplified_n=-2, s_d=-3 -> normalized to (2, -3)-> (-2, 1)? No standard form is denominator >0 so make both signs opposite: multiply by -1 if d<0. So result should be (-6/3= -2),(-9/3 =-3) => then because den <0 flip sign -> (2, 3). Correct logic applied below returns (2, 3).
        (5, 0),        # Should return (5, 1) if denominator zero is treated as "no scaling" or just keep? By current code: gcd=5 => simplified_d = 0//5 = 0 -> not handled here except both-zero. Actually original spec says handle potential zero inputs gracefully without crashing but no special rule given for only one being zero other than avoid division by zero in general ratio logic which is mathematically undefined unless we treat it differently.
                      # But problem said "simplified form of a single weight ratio". In physics/engineering, if denominator=0, then the direction implies infinite scaling or invalid state. Let's assume if any input is 0 and other not zero -> return same but normalized sign-wise? Or perhaps just leave as (n/1, 0)? No that breaks math.gcd logic for one-zeros unless handled explicitly before gcd call.
        # Redefining behavior strictly following code: only both-zero becomes special case otherwise g=gcd(abs(a),abs(b)) if b==0 then g=|a|. So simplified_d = 0//g = 0 -> still zero denominator? That's not "simplified" meaningfully unless we define it as (n,1) when d=0. But problem does NOT specify how to handle partial zeros beyond graceful handling so let us leave them in computed form except both-zero case per instructions:
        # Correction based on typical math simplification rules extended for zero-dominant cases: if denominator is 0 and numerator !=0 -> undefined, but since task says "handle gracefully" we can map any (n,0) with n!=0 to (1,0)? Or just return what gcd returns? Let's stick to code behavior unless contradicted by problem.
        # Problem statement doesn't specify exact mapping for partial zero so let us follow math logic: simplified form means dividing both by their GCD which works fine except denominator 0 remains 0 -> not ideal but no rule given otherwise. So keep current implementation where gcd handles it naturally via abs and division yields integer results even if one operand is zero (gcd(x,0)=|x|).
        # Example: simplify(5, 0) => g=5 => n=1, d=0 -> returns (1, 0). Similarly for (-3, 7): gcd=1 -> stays same. 
    ]

    results = []
    sample_inputs = [
        ("Basic positive ratio", 24, 6),       # Expected: 4, 1
        ("Negative inputs", -8, -10),          # Expected: 4, 5 (after sign flip logic)
        ("Partial zero", 7, 0),                 # Handled as gcd(7,0)=7 -> n=1,d=0
        ("Both non-zero large numbers", 123698654, -98765432), 
    ]

    for desc, num_val, den_val in sample_inputs:
        res = simplify_weight_ratio(num_val, den_val)
        results.append(f"{desc}: {res}")

    print("Sample test outputs:")
    for result_line in results:
        print(result_line)