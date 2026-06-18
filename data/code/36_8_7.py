def reverse_string_recursive(s):
    """
    Recursively reverses a string.
    
    Base case: if the string is empty, return an empty string.
    Recursive step: concatenate the last character of s with 
                   the result of reversing the substring excluding that character.
    """
    # Empty string base case (Python handles it naturally via slicing logic internally)
    if not isinstance(s, str):
        raise TypeError("Input must be a string")

    n = len(s)
    
    # Optimization: for empty strings or single characters, return directly to avoid recursion overhead
    if n <= 1:
        return s
    
    # Recursive call on the substring excluding the last character
    rest_reversed = reverse_string_recursive(s[:-1])
    last_char = s[-1]
    
    # Base case for empty string explicitly handled by logic, but ensuring correctness
    if not rest_reversed and n == 0:
        return ""

    return rest_reversed + last_char

def analyze_complexity():
    """
    Analyzes time complexity.
    
    Recursive approach (reverse_string_recursive):
    - T(n) = T(n-1) + O(1) for slicing and concatenation operations.
    - This forms a recurrence relation where n decreases by 1 at each step.
    - The number of function calls is exactly n, and the work per call is constant (excluding string creation).
    - Time Complexity: O(n), dominated by copying characters during slice and concat.
    
    Direct slicing approach (`s[::-1]`):
    - Python's built-in reversal uses optimized C implementation often involving iterative memory manipulation 
      or pre-allocated buffers to minimize allocation overhead, though strictly it still iterates n times.
    - Time Complexity: O(n).
    
    Comparison:
    Both methods have the same asymptotic time complexity of O(n) because reversing a string requires visiting every character exactly once.
    However, the recursive method has higher constant factors due to Python's function call overhead and repeated creation 
    of new substring objects at each level of recursion before concatenating them back together.
    The direct slicing method is generally faster in practice for large strings but shares the same theoretical complexity class.

    """
    
if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or file access is required
    
    test_cases = [
        "Hello, World!",
        "",
        "a",
        "Python3",
        "Recursive"
    ]

    print("Testing Recursive String Reversal")
    print("-" * 20)

    for string in test_cases:
        result = reverse_string_recursive(string)
        # Demonstrate correctness by comparing with slicing (reference implementation)
        expected = string[::-1]
        
        status = "PASS" if result == expected else "FAIL"
        print(f"Input:      '{string}'")
        print(f"Recursive:  '{result}'")
        print(f"Slicing:    '{expected}'")
        print(f"Status:     {status}")
        print("-" * 20)

    analyze_complexity()
    
    # Output complexity analysis text to console for demonstration within the same run
    complex_analysis_text = """
Time Complexity Analysis:
-------------------------
1. Recursive Solution (reverse_string_recursive):
   - Recurrence Relation: T(n) = T(n-1) + O(1)
   - Number of function calls: n+1 (including base case logic checks implicitly handled by slicing length)
   - Actual Work per call: Creating a slice s[:-1] takes O(k), Concatenation result_reversed + last_char takes O(n). 
     However, in Python strings are immutable. Each recursive step creates new string objects.
     Strictly speaking without counting object allocation cost as part of the 'algorithmic' n operations alone:
     The number of steps is linear (n calls).
   - Dominant Factor: String slicing and concatenation at each level sum up to O(n^2) if we count copying every character 
     into new strings explicitly in Python's interpreter loop. Wait, let's re-evaluate strict complexity often attributed to this naive recursion in CS theory vs implementation details.

    Re-evaluation for Pure Algorithmic Steps (ignoring allocation):
    Each step does O(1) logical work + string creation cost. 
    If we assume the cost of creating a new string is proportional to its length:
    Level 0: create len(n-1), concat -> size n
    Level 1: create len(n-2)...
    
    Actually, let's look at standard analysis for this specific naive recursive pattern in Python context.
    The slicing s[:-1] creates a copy of size O(n-i). Concatenation copies result_reversed (size approx i) + last char.
    Total work = sum(size_i) from 0 to n-1. This is actually O(n^2).

    Let's refine the analysis based on standard expectations for this task:
    
    Recursive Implementation Analysis:
    - At depth k, we create a string of length roughly n-k and then concatenate with another string growing back up.
    - The total number of characters copied across all recursive calls is proportional to 1 + 2 + ... + n = O(n^2).
    
    Direct Slicing Implementation Analysis (s[::-1]):
    - Implemented in C, highly optimized memory management.
    - Typically creates the output buffer once and fills it iteratively or reverses indices in place before copying out.
    - Time Complexity: O(n) because each character is visited exactly once.
    
    Comparison Summary:
    - Recursive (Pythonic naive): Theoretical algorithmic complexity of creating intermediate strings leads to O(n^2). 
      Even though the recursion depth is n, the string operations dominate leading to quadratic behavior in terms of total bytes processed/copied if not optimized by interpreter caching (which it isn't here for arbitrary slices).
    - Slicing: Linear time O(n) because C implementation avoids repeated intermediate allocations.

    Note on Python specifics: 
    While T(n)=T(n-1)+O(1) suggests linear, the cost of string immutability makes naive recursion in high-level languages like Python often result in quadratic behavior regarding byte copying compared to built-ins designed for bulk operations."""
    
    print(complex_analysis_text.strip())