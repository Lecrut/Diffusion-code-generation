import math

def simplify_ratios(ratio1: tuple[int], ratio2: tuple[int]) -> tuple[tuple[int, int], str]:
    """
    Calculates the simplified ratio between two pairs of weights using their GCDs individually.

    Args:
        ratio1 (tuple): A tuple containing two integers representing the first weight pair.
        ratio2 (tuple): A tuple containing two integers representing the second weight pair.

    Returns:
        tuple: A tuple containing:
            - The simplified form of ratio1 as a single GCD-reduced pair if they were compared, 
              or individual simplified pairs for each input if treated independently per component logic requested.
              However, based on "simplified ratio in its lowest terms" between two inputs implies comparing them?
              Re-reading the prompt: "calculates the simplified ratio". Usually ratios are A:B and C:D -> (A/C):(B/D).
              But GCD is applied to reduce fractions. Let's interpret as normalizing each pair individually first,
              then potentially a combined comparison or just returning normalized forms? 
              
              Actually, standard interpretation of "ratio" with two inputs often means finding the common relative scaling OR reducing them separately.
              Given "using the greatest common divisor", it most likely implies:
              1. Reduce ratio1 to its simplest form (a/b -> a/gcd(a,b), b/gcd(a,b))
              2. Reduce ratio2 similarly.
              
              Or, if they represent two sides of a combined problem? 
              Let's assume the task wants us to return the simplified forms of both inputs as separate normalized tuples,
              or perhaps combine them into one big fraction (w1_1 / w2_1) and reduce that?
              
              The prompt says: "calculates THE simplified ratio". Singular. This suggests comparing Ratio1 vs Ratio2 directly?
              Example: R1 = (a,b), R2 = (c,d). Is the result a/c : b/d ? Then simplify THAT pair? 
              Let's assume we calculate the cross-ratio or simply reduce each component to simplest terms relative to their own,
              but usually "ratio of two ratios" isn't standard without context.
              
              Most robust interpretation for "two weight ratios ... calculates THE simplified ratio":
              It likely means taking the first numbers and second numbers as a single compound fraction (a/c : b/d) -> (ad/bc)? No, that's complex.
              
              Let's stick to the most logical mathematical operation provided GCD context: 
              Normalize both input pairs individually to their lowest terms using their own GCDs.
              Then return both simplified forms? Or maybe compare them?
              
              Wait, "calculates THE simplified ratio" (singular).
              If inputs are A:B and C:D. Maybe it wants the relationship between them? 
              Let's assume the user has two sets of weights [w1_1, w2_1] and [w1_2, w2_2].
              Perhaps they want to compare component-wise: (A/C) : (B/D)? No.
              
              Alternative interpretation: The input is a single ratio expressed as two numbers? 
              "accepts TWO weight ratios". So Input 1 = Ratio A, Input 2 = Ratio B.
              Maybe the goal is to find if they are equal after simplification? Or just output both simplified versions?
              
              Let's re-read carefully: "calculates THE simplified ratio in its lowest terms". 
              This phrasing often applies when you have a single fraction or vector and reduce it. 
              Here we have two ratios. A common task is to compare them by reducing each, then checking equality, 
              OR converting them into a form where they share the same denominator?
              
              However, without specific instructions on HOW to combine two ratios (like addition/subtraction), 
              the only safe "calculation" using GCD for individual inputs provided as arguments is:
              1. Reduce Ratio A by gcd(A[0], A[1])
              2. Reduce Ratio B by gcd(B[0], B[1])
              
              But why two inputs then? Maybe calculate the ratio of their sums? Or product? 
              Let's assume the task implies finding a unified reference or simply normalizing both to compare them implicitly, 
              but returning the normalized states is safer if no operation is defined. 
              
              Actually, looking at typical coding challenges: "Given two ratios, simplify them".
              But it says "calculates THE simplified ratio". Singular.
              Could it be (Ratio1[0] / Ratio2[0]) : (Ratio1[1] / Ratio2[1])? No, division might yield floats. Keep integers -> cross multiply? 
              
              Let's try a different angle: Maybe the inputs are actually one single ratio split into two parts to represent numerator and denominator components across scenarios?
              Unlikely.
              
              Best guess for "THE simplified ratio" from TWO ratios:
              Perhaps it means calculating the GCD of all 4 numbers together? No, that loses structure.
              
              Let's assume the user wants to simplify each pair independently because they represent two distinct weight configurations (e.g., before and after), 
              and outputting both is necessary contextually if no combined operation exists. 
              However, strictly following "calculates THE... ratio", maybe it implies comparing them? 
              
              Let's provide a solution that:
              1. Simplifies Ratio1 to its lowest terms (a/gcd : b/gcd).
              2. Simplifies Ratio2 similarly.
              Returns both as the result tuple if they are different, or just one representation?
              
              Wait, maybe "two weight ratios" means a list of two items where each item is a ratio? 
              And we need to output the simplified version of THAT input data structure?
              Yes! Input: ((a,b), (c,d)). Output: Reduced((a/gcd(a,b), b/gcd(a,b)), (c/gcd(c,d), d/gcd(c,d))).
              
              Let's implement this logic: Normalize both tuples independently.
    """
    
    def get_simplest_pair(pair):
        a, b = pair[0], pair[1]
        if a == 0 and b == 0: return (0, 0) # Handle undefined edge case simply
        common_divisor = math.gcd(a, b)
        return (a // common_divisor, b // common_divisor)

    simplified_pair_1 = get_simplest_pair(ratio1)
    simplified_pair_2 = get_simplest_pair(ratio2)

    # If the prompt implies a single output ratio derived from two inputs without explicit operation definition:
    # We will return the list of both simplified tuples, as "THE" might refer to the set resulting from processing.
    # Or perhaps it expects us to treat them as one big fraction? 
    # Let's assume the safest interpretation for a generic script: Normalize both and return them together or just normalized forms.
    
    # Re-evaluating based on strict singular "THE simplified ratio":
    # Is there an operation missing? Addition of ratios (a/c + b/d)? That requires common denominator which is messy with integers without scaling up first. 
    # Let's assume the task meant: Normalize both inputs individually and return them as a structured result, 
    # or perhaps the user considers "the ratio" to be the collection of these two simplified states.
    
    # Given the ambiguity, I will normalize each input pair independently using GCDs on their respective components.
    # If they represent a single complex fraction (w1/w2 and w3/w4), usually one doesn't have an operation unless specified. 
    # However, often "ratio" in plural inputs context implies checking equivalence or just formatting.
    
    return (simplified_pair_1, simplified_pair_2)

if __name__ == '__main__':
    # Sample values as tuples of integers
    ratio_a = (60, 84)   # Example: simplifies to 5 : 7
    ratio_b = (90, 130)  # Example: simplifies to 9 : 13
    
    result_simplified_ratio = simplify_ratios(ratio_a, ratio_b)

    print(f"Original Ratios:")
    print(f"Ratio A ({ratio_a}) -> Simplified: {result_simplified_ratio[0]}")
    print(f"Ratio B ({ratio_b}) -> Simplified: {result_simplified_ratio[1]}")
    
    # Optional check for equality if they were meant to be compared
    is_equal = result_simplified_ratio[0] == result_simplified_ratio[1]
    print(f"\nAre the simplified ratios equal? {is_equal}")