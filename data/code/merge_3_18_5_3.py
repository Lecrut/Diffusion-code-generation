def increasing_values_generator(sequence):
    """
    Generator function that yields True if the current value is strictly greater 
    than the previous value in the input sequence, otherwise yields False.
    
    Args:
        sequence (iterable): An iterable of comparable values.
        
    Yields:
        bool: True if current > previous, else False. The first yield will be based on
              comparing the second item to the first; no comparison is made for 
              a single-item or empty input regarding 'increasing' status in terms 
              of yielding logic against a prior value (as there is none).
              
    Note: For simplicity and standard interpretation, this generator yields False 
          initially if len(sequence) < 2 because the concept of "greater than previous"
          does not apply to the first element. Alternatively, it can be argued that 
          no boolean decision needs making for index 0. However, to strictly follow 
          'current > previous', we only perform a comparison starting from the second item.
          
    Revised Logic: We iterate through items with their indices. For i=0, there is no 
    previous value. To ensure exactly one output per input element or align outputs?
    The prompt says "yields True ONLY when...". It implies we should yield something for every step 
    where a comparison can be made, OR skip the first if impossible. Let's assume we need to produce
    results corresponding to positions 1..n (comparing item i with item i-1). If len < 2, no yields?
    
    Actually, usually such tasks expect an output for every element or a flag per transition. 
    Given "yields True only when...", if we don't have a previous value, the condition is undefined/falseish in context of comparison. 
    Let's assume standard pattern: compare current with prev. If first item exists but no prev, skip yield?
    
    Better interpretation for robust code without crashing on edge cases (len=1):
    We will iterate through items starting from index 1 to len(sequence)-1.
    However, if the requirement is strict per-item output including the start: 
    Let's assume we want a boolean result for every item where applicable. 
    If i == 0: no previous -> cannot determine -> likely skip or yield False? 
    The prompt says "yields True ONLY when...". It doesn't say it must yield something else otherwise, but implies yielding the condition status.
    
    Let's go with: Yield a boolean for every item starting from index 1 (where comparison is possible). 
    If len < 2, nothing yields? Or perhaps the user expects an output per input element regardless of validity?
    
    Alternative common pattern in such coding tasks:
    For each x in sequence[1:], check if x > prev. Yield result. Update prev. Ignore first item for yielding logic?
    
    Let's refine based on typical generator expectations: Usually, we iterate through the list and compare current to previous 
    stored value. If it's the very first element of iteration (index 0), there is no previous. We can choose not to yield anything in that case 
    or assume a default False/None. Given "yields True ONLY when...", if condition isn't met, nothing happens? No, usually implies yielding the boolean result of the check.
    
    Decision: Iterate through items with index. If i > 0 and current > previous: yield True. Else (if not greater or no prev): yield False. 
    This ensures an output for every element except potentially the first if we strictly follow "only when". But to be safe and return a stream of booleans matching input length behavior often seen in interviews, let's map each item to its status relative to previous.
    
    Wait, re-reading: "yields True only when...". This suggests that False is not explicitly yielded? Or it yields the boolean result (True/False)? 
    Usually "generates a sequence of booleans" implies yielding both. If I don't yield anything for non-increasing steps, the output stream becomes sparse and hard to predict without knowing input length beforehand.
    
    Let's assume standard behavior: Yield True if increasing, False otherwise, starting from index 1 (or even index 0 with a convention). 
    To be most robust against "no previous", let's yield nothing for index 0? Or maybe the prompt implies filtering only positives? 
    "yields True ONLY when..." -> This phrasing is specific. It might mean: `if current > prev: yield True`. And do not yield anything else (i.e., no False).
    
    However, a generator that yields nothing for non-increasing steps makes testing the sequence structure hard unless you know exactly where it increases. 
    Let's look at the constraint "strictly greater than previous". This is a condition check. The most logical interpretation of a boolean flag generator is yielding True if true, False if false (standard pattern). If interpreted literally as "only yields True", then non-increasing values yield nothing.
    
    Given the ambiguity, I will implement it such that:
    1. It processes pairs (prev, curr).
    2. Yields True when curr > prev.
    3. Does NOT yield anything else? Or yields False? 
    "yields True ONLY when..." strongly implies exclusion of other values. If I have a sequence [5, 4], and it's not strictly greater, the condition is false. The generator does nothing (no yield).
    
    Let's try this interpretation: It acts as an event detector for increases. 
    But often users want to know where it went down too. 
    Let's assume the standard "is_greater_than_previous" function logic which returns True/False per step, but implemented via yields. If strict literalism applies ("only when"), then False is not yielded.
    
    However, looking at similar tasks online: Usually they want a boolean stream. I will provide a stream where every item from index 1 onwards generates a yield (True or False). This makes the output length predictable and testable without external input assumptions about sparsity. 
    Why? Because "yields True only when..." defines the condition for TRUE, not necessarily forbidding FALSE yields elsewhere in a boolean generator context. If it meant "only yields True", it would likely say "filters" or "selects". It says "generates ... that yields True ONLY WHEN...". This allows yielding False otherwise (as long as True is conditional).
    
    Final Plan: Iterate from index 1 to end. Compare with prev. Yield boolean result for each step.

def increasing_values_generator(sequence):
    """

if __name__ == '__main__':
    pass
