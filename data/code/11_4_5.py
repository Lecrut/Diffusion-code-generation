from math import gcd

def simplify_ratio(num: int) -> float:
    """Simplify a ratio given as an integer numerator to its simplest form (as float)."""
    if num == 0:
        return 0.0
    abs_num = abs(num)
    divisor = gcd(abs_num, abs(1)) # Simplifying x/1 -> x/1 is just returning the number itself in a conceptual ratio sense for this problem context where input is (a,b). 
                                    # Actually re-reading: "list of length pairs". Example [(a1,b1), ...].
    # The prompt asks to return simplified ratios. A common interpretation for pair lists without denominators provided explicitly as floats but implied 1, or perhaps the user wants a/b.
    # Let's interpret (a, b) as representing the ratio a:b -> float value = a / b in simplest terms if integers are given.
    pass

def get_simplified_ratios(pair_list: list):
    """
    Accepts a list of length pairs and returns a list of simplified ratios.
    
    A pair (a, b) is interpreted as the ratio 'a to b'. 
    We calculate a / b. If both are integers, we can try to represent them cleanly, 
    but since Python's float handles division well, we will return the floating point value 
    representing that ratio in its simplest numerical form.
    
    Alternatively, if the task implies keeping it as an integer fraction when possible:
    We will assume the input pairs are integers (a, b) and calculate a/b reduced by dividing both numerator/denominator by their GCD, then return the resulting float or a tuple representing the simplified terms. 
    Given "returns a list of simplified ratios", returning floats is standard unless specific format requested which isn't here.
    However, to be precise about 'simplified', if we have (4, 8), ratio is 0.5. If (-2, 3), it's -0.66... 
    Let's assume the output should be a list of floats representing a/b simplified by common factors first?
    
    Actually, simpler: Just return a / b as a float for each pair. The "simplified" part usually applies if we were to represent them strictly (p/q) where gcd(p,q)=1 and q>0. 
    Let's implement the GCD reduction logic just in case they want the canonical form before division or perhaps an integer representation?
    
    Re-reading carefully: "returns a list of simplified ratios". 
    If I have 2/4, that simplifies to 1/2 = 0.5. 
    Let's return the float value directly as it is inherently unique for any real number ratio in standard contexts unless symbolic form is requested (which requires fractions module and isn't strictly 'Python built-in' only).
    
    Wait, "list of length pairs". Input: `[(a1, b1), ...]`. 
    Maybe the user wants to output tuples `(p, q)` where p/q = a/b and gcd(p,q)==q_sign? No, usually ratio implies value.
    Let's provide two options internally but return float for simplicity unless specific requirement is missed. 
    Actually, let's look at similar tasks often implying "reduce the fraction".
    
    If input `[(2, 4)]`, output `[0.5]`.
    Input `[(1, -3)]`, output `[-0.333...]`? Or maybe keep signs separate? 
    Let's stick to standard float division of a by b.
    
    Correction: Often these tasks want the reduced integer numerator and denominator if inputs are ints. But "returns ... ratios" usually implies the value.
    However, to be robustly 'simplified', let's return the tuple `(reduced_num, 1)`? No.
    Let's assume the standard definition: The ratio of a to b is simply `a/b`. 
    If we interpret "simplified" as reducing fractions before division (useful for precision if working with large ints):
    
    Example logic: 
    g = gcd(a, b) -> num=a//g, den=b//g. Result float(num/den).
    This handles negative numbers correctly by GCD behavior? Python's math.gcd returns positive divisor usually >= 1 unless arguments are 0 (which is special case above).
    
    So: 
    For each (a, b):
      g = gcd(a, b) -> wait if one is zero this fails. Handle zeros manually.
      If a==0 or b==0 return specific values? Or just raise error? The prompt doesn't specify input validation constraints beyond "list of length pairs". Let's handle 0 gracefully. 
      
    Final decision: Return the simplified float value a/b, calculated after reducing the fraction to lowest terms by dividing both numerator and denominator by gcd(|a|, |b|). This ensures mathematical simplification before division.
    
    """
    results = []
    for num_pair in pair_list:
        if len(num_pair) != 2:
            raise ValueError(f"Each pair must have exactly two elements, got {len(num_pair)}")
        
        a, b = num_pair
        
        # Handle zero cases specifically to avoid division by zero or trivial gcd issues with negatives? 
        # math.gcd(0, x) returns abs(x). So it works.
        try:
            divisor = gcd(a, b) if (a != 0 or b != 0) else 1
            
            # Reduce terms
            reduced_a = a // divisor
            reduced_b = b // divisor

            # If denominator becomes zero after reduction, it means original was like x/0. 
            # We handle the division safely here to produce 'inf' or error? 
            # Standard float('inf') for x/0 where x!=0 is acceptable in many contexts unless strict math required.
            
            ratio = reduced_a / reduced_b if reduced_b != 0 else (float('inf') * (-1) if a < 0 and b == 0 else float('-inf') if a > 0 and b == 0 else 0.0)
            
            # However, simpler approach for general purpose: just return the value. 
            # The reduction step ensures that we don't have precision issues with very large integers where direct division might behave oddly in some specific big-int libraries (though Python floats handle arbitrary magnitude reasonably well).
            results.append(ratio)
        except ZeroDivisionError:
            # If b is 0, the ratio is undefined. We'll return float('inf') or similar? 
            # Given no constraints on output for invalid input, let's raise or use inf. Let's use float('inf').
            if a < 0 and b == 0: results.append(float('-inf'))
            else: results.append(float('inf'))

    return results

if __name__ == '__main__':
    # Hard-coded sample values that do not require input, network or files.
    samples = [
        (4, 8),   # Should simplify to 0.5 (2/4 -> 1/2)
        (-3, 6),  # -0.5
        (7, 1),   # 7.0
        (0, 5),   # 0.0
        (5, 0),   # Infinity or undefined? Let's output float('inf')
    ]

    print("Input Pairs:", samples)
    simplified = get_simplified_ratios(samples)
    print("Simplified Ratios:", simplified)