import math

class GeometryCalculator:
    """A class designed for geometry calculations involving right triangles."""

    def calculate_side_ratio(self, side_a: int, side_b: int) -> float:
        """
        Calculates the ratio of two sides (a/b and b/a) for a right triangle.
        
        Since the problem asks to ensure the result is simplified using GCD,
        we will simplify both ratios 'a/b' and 'b/a' by dividing numerator 
        and denominator by their greatest common divisor if they represent integers,
        but since float division cannot be directly simplified via integer GCD in a floating point context,
        this method returns the primary ratio (side_a / side_b) represented as an irreducible fraction.
        
        To return the 'simplified' result compatible with standard output expectations 
        while adhering to the instruction of using GCD, we will:
        1. Compute integers representing numerator and denominator.
        2. Calculate their GCD.
        3. Return the float value but also provide access to simplified integer parts if needed externally,
           or simply return the float which is standard for ratio calculations unless specific precision/simplified fraction logic is required as a string representation.
           
        However, strictly interpreting "result is simplified using the GCD" implies returning 
        either the tuple of simplified numerator/denominator or ensuring internal consistency.
        Given Python's nature with floats vs integers:
        
        We will return the float result but internally demonstrate the simplification logic 
        by constructing a fraction and converting it back, handling integer inputs specifically.

        Args:
            side_a (int): The length of one leg of the right triangle.
            side_b (int): The length of the other leg of the right triangle.

        Returns:
            float: The ratio of side_a to side_b. If both are integers, this returns 
                  a/float(b). If specific simplified fraction representation is desired via integer logic,
                  it can be inferred that for large numbers where floating point precision loses info about simplification,
                  one might want the exact form. But standard float division doesn't preserve GCD state visually.

        Note: For this implementation to strictly follow "result is simplified", we treat input as integers 
        and perform integer reduction logic if possible or just perform the division cleanly.
        
        Re-evaluating based on strict interpretation of 'simplified using gcd':
        Usually, ratios like 3/5 become (1 * k) / (2k). Here inputs are sides.
        Let's return a tuple (numerator_reduced, denominator_reduced) if exact division is possible? 
        No, ratio usually implies float in this context unless specified as Fraction class usage which isn't imported yet.

        Decision: Return the float value but utilize GCD to verify no common integer factors were 'lost' before decimal conversion logic (though decimals always lose precision).
        
        Actually, let's provide a helper method or just use math.gcd to simplify the inputs if they share a factor? 
        No, sides don't necessarily have a shared factor relative to each other that simplifies their ratio like 2/4 -> 1/2.
        Yes! That is exactly what 'simplify using GCD' means for a ratio of two integers.
        
        Example: Side A = 8, Side B = 4. Ratio = 2. Simplified form? 
        Or if Side A=6, Side B=9 -> Ratio = 0.66... which is 2/3.
        
        So the task implies converting the integer ratio a/b into irreducible fraction terms (num/den) using GCD(a,b).

        Final Plan: Return a tuple representing the simplified numerator and denominator if we assume exact rational arithmetic, 
        but since return type hint says float in my head earlier... let's look at the prompt again.
        "calculates ... ratio" -> usually float. 
        "...result is simplified using GCD".

        Interpretation: The output should ideally represent the simplest form of a/b and b/a? 
        Or just that we use GCD to ensure clean math.
        
        Let's implement it such that if inputs are integers, we compute gcd(a,b) = g.
        Then simplified numerator is a//g and denominator is b//g (or vice versa).
        But returning these as floats? No, fractions are often represented as tuples or strings in Python math unless using Fraction class.

        Let's assume the user wants to see if we can reduce 8/12 -> 2/3 logic applied here.
        
        However, standard float output of a/b is not "simplified" visually (e.g., 0.66... doesn't show 2/3).
        
        Let's return the tuple `(side_a // gcd_val, side_b // gcd_val)` where `gcd_val` = math.gcd(side_a, side_b) 
        if we want to strictly represent "simplified fraction", but that might not be a float ratio.

        Alternative: Just calculate the float and mention the GCD step in comments/variable names?
        
        Let's try to interpret this as returning the simplified fractional components since floats don't carry 'simplification' metadata natively without losing info (e.g. 2/3 vs 4/6).

        Okay, I will return a tuple of `(reduced_numerator, reduced_denominator)` calculated via GCD if inputs are integers.
        This satisfies "result is simplified using the GCD" better than just `a/b`."""
        
        # Handle case where input might be floats (unlikely for geometry side lengths in integer problems usually)
        try:
            a = int(side_a)
            b = int(side_b)
            
            if not isinstance(a, int): raise ValueError("Input must support conversion to integers")
            
            common_divisor = math.gcd(int(side_a), int(side_b))
            
            # Simplified numerator and denominator relative to each other? 
            # Wait, ratio of two sides. A/B vs B/A.
            # Usually we just take a/b or b/a. Let's provide the primary direction (a over b).
            # But technically "ratio" can be bidirectional contextually.
            # I will return both simplified forms if possible? Or just one standard form?
            
            # The prompt says "calculates THE ratio". Singular. 
            # Implies side_a / side_b or maybe min/max logic to avoid >1? 
            # Let's do a/b normalized by their own GCD which effectively reduces the fraction representation of that specific division result IF it was an integer pair reduction like 8/4 -> 2 (but float handles integers too).
            
            # Actually, if I have 6 and 9. gcd is 3. 
            # Ratio as int fractions: 2/3 or 3/2.
            # Let's return the tuple representing this simplified fraction to ensure correctness of "simplified using GCD".
            num = a // common_divisor
            den = b // common_divisor
            
            return (num, den) if isinstance(a, int) and isinstance(b, int) else side_a / side_b
        
        except Exception: 
             # Fallback to float division for non-integers or errors in logic
            return float(side_a) / float(side_b)

if __name__ == '__main__':
    # Sample values hardcoded as per requirements.
    calc = GeometryCalculator()

    # Example 1: Simple integer ratio that simplifies nicely (e.g., 8 and 4 -> 2/1 or just 2?)
    a, b = 6, 9
    
    result_tuple = calc.calculate_side_ratio(a, b)
    
    print(f"Side A ({a}) / Side B ({b}):")
    if isinstance(result_tuple, tuple):
        # Display as reduced fraction for integer inputs
        num_val, den_val = int(round(float(result_tuple[0]))), int(round(float(result_tuple[1]))) 
        # Recalculate strictly from args to avoid float confusion in print logic above (though result is already simplified ints)
        import math
        gcd_val = math.gcd(a, b)
        simple_num = a // gcd_val
        simple_den = b // gcd_val
        print(f"Simplified Fraction: {simple_num}/{simple_den}")
    else:
        # Display as float for non-integer inputs or standard usage
        val = result_tuple
        if isinstance(val, tuple): # If logic above returned tuple in some branches? 
            pass
        
        # Refined printing based on expected return type adjustment from docstring analysis
        # The method returns (num, den) for ints. Let's print that clearly.
        
    # Example 2: Non-perfect simplification or float result
    
    a2, b2 = 5,