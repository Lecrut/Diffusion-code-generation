def simplify_ratios(weight_rations):
    """
    Takes a list of weight ratios (each as two integers) and returns 
    a new list containing their simplified forms.
    
    A ratio is represented by an index or tuple in the input list:
    - If passed as [a, b], it represents the ratio a:b.
    - The function simplifies each pair to its lowest terms.

    Args:
        weight_rations (list): List of lists/tuples containing two integers representing weights.
        
    Returns:
        list: New list with simplified ratios represented as tuples [a, b].
    
    Example:
        >>> simplify_ratios([[2, 4], [3, 6]])
        [[1, 2], [1, 2]]
    """
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return abs(a)

    result = []
    
    for ratio in weight_rations:
        if isinstance(ratio[0], int) and len(ratio) == 2:
            w1, w2 = ratio
            
            # Ensure positive GCD by handling signs correctly
            common_divisor = gcd(w1, abs(w2))
            
            simplified_w1 = w1 // common_divisor
            simplified_w2 = w2 // common_divisor

            result.append([simplified_w1, simplified_w2])
        else:
            # Fallback for other potential input formats if needed (e.g. tuple)
            ratio_tuple = list(ratio[:2])

if __name__ == '__main__':
    pass
