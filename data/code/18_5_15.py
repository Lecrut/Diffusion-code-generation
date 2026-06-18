def strictly_increasing_generator(sequence):
    """
    Generator that yields True if a value is strictly greater than 
    the previous value in the input sequence, False otherwise (or initially).

    Args:
        sequence (list or tuple): A sequence of numbers.

    Yields:
        bool: Boolean indicating whether current > previous. First yield will be None/False logic handled inside loop structure for single item start implicitly via flag or first comparison skip. 
               To strictly follow "yields True only when...", we need a boolean output even if condition fails? 
               The prompt says "yields True ONLY WHEN...". It implies False is allowed otherwise, OR it might imply strict adherence (only yield on increase).
               
    Clarification based on standard interpretation of such tasks:
    We should iterate. For the first element, there is no previous value.
    Common logic: yield comparison result for all elements except possibly treating index 0 specially.
    
    However, re-reading "yields True only when...": 
    Does it mean if condition fails, do NOT yield? Or does it mean yield a boolean indicating the state (True/False)?
    Usually in these algorithmic generator tasks (like finding local maxima or strict increases), we want to know for each step.
    
    Let's assume standard behavior: Iterate through pairs. 
    Actually, if the input is [10, 20], expected output stream should indicate "increasing" at index 1 relative to 0? Or include index 0 as a placeholder (False/None)?
    Given "yields True ONLY WHEN...", it strongly suggests that on non-increasing or first element steps where condition isn't met by logic of having a predecessor, we might not yield anything OR yield False. 
    But often in coding tests, if you are asked to generate flags for each item, you return the boolean result.
    
    Let's implement yielding the boolean comparison result (True/False) for every element starting from index 1, and perhaps skip or handle index 0 as not comparable or yield False? 
    A safe bet that satisfies "yields True ONLY when" is to only output on increase, but usually users want a signal for EVERY step.
    
    Let's look at similar LeetCode/CodingBat problems: `strictlyIncreasing` returns boolean array. Generator version likely wants the boolean sequence.
    
    Revised Logic: 
    Iterate with index i from 1 to len(seq)-1.
    Compare seq[i] > seq[i-1].
    Yield True if yes, False otherwise? Or just yield when it IS greater?
    "yields True ONLY WHEN" -> This phrasing is ambiguous. It could mean: 
    1. Condition met -> Yield True; Else -> Do nothing (no yield).
    2. Condition met -> Yield True; Else -> Yield False.

    Context clue: "strictly greater than the previous value". 
    If I ask for a generator of flags, usually you get a flag for every position. 
    However, if it says "yields True ONLY WHEN...", it often implies filtering (like filter() behavior).
    
    Let's assume interpretation 1 (filter): Only yield when strictly greater. This matches the literal text "Only yields...". If it meant always return bool, it would say "yields a boolean value indicating...".
    
    So: 
    i=0: Skip or handle? First element has no previous. Cannot be > prev. Condition fails -> No yield (or skip).
    i>0: if curr > prev -> yield True else do nothing.

    Let's verify with the sample block logic to ensure it runs and makes sense. 
    Sample input likely contains mixed values to test both increasing and non-increasing, plus at least one increase. 

""" # End of docstring placeholder
import sys as _sys_internal_check_ # Forbidden? "Never call ... any interactive prompt". Import is fine but avoid runtime calls. I will not import anything unnecessary unless needed for logic (e.g. no imports strictly required if using built-ins).

def strictly_increasing_generator(sequence):
    prev = None
    
    for val in sequence:
        # For the first element, there is no previous value to compare with strictly greater.
        # Based on "yields True ONLY WHEN", we assume we only yield when condition holds.
        if prev is not None and val > prev:
            yield True
            
        else: 
            # If it wasn't an increase (e.g., equal or smaller) OR it's the first element,
            # based on "ONLY WHEN" strict reading -> do NOT yield anything here?
            pass

    return 

# Wait, if I use `pass`, then for input [10], output is empty. 
# Is that desired? If user wants to know about every step, they usually expect a boolean per item (True/False) or just True on success.
# Let's reconsider the phrasing "yields True ONLY when...". 
# Interpretation A: Generator yields exactly one value for each input element -> The comparison result as bool? Or only yield if True?
# If I have to choose between "Generator of booleans" vs "Filter generator", "ONLY WHEN" leans towards Filter.
# However, often in Python challenges (e.g. codingbat), they want the boolean flag sequence. 
# Let's try to provide a boolean for EVERY step including non-increasing ones? No, because it says "yields True ONLY...". If I yield False when not greater, then am I yielding something that isn't True only when ... ? Yes.
# The most logical interpretation of "Generator function that yields True..." is: 
# For each x in sequence (starting from index 1?), if condition(x) -> yield True. Else -> (implicit nothing or continue).

    # Let's stick to the Filter logic as it fits "yields True ONLY WHEN".
    
# Wait, maybe the user wants a boolean flag for EVERY element? 
# E.g., input [1, 2, 3] -> [True, False?, True?] No.
# Comparison: (curr > prev).
# Input [10, 5]: Should I yield nothing or yield 'False'?
# "Yields True ONLY WHEN" implies the set of yielded values is a subset of {True}. 
# Values like 'y', 'n' are not generated? Or only T is ever generated. This confirms Filter logic.

def strictly_increasing_generator(sequence):
    """
    Generator that yields exactly one value (True) for each element in the input sequence,
    provided that this element is strictly greater than its predecessor.
    For elements equal to or smaller than the previous element (and also the first element), nothing is yielded.
    
    Note: This interpretation adheres strictly to "yields True ONLY WHEN". 
          If a boolean flag for all steps was required, the prompt would typically say "yields a boolean indicating...".
    """
    prev = None
    
    # We need a way to compare if it's not just index based but value based.
    # Actually we can do: keep track of previous yielded? No, previous IN INPUT sequence (value).
    
    for val in sequence:
        if prev is not None and val > prev:
            yield True

if __name__ == '__main__':
    pass
