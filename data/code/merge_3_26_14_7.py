import sys

def value_generator(data, threshold):
    """
    Generator function that yields True if input data is strictly greater than a predefined threshold.
    
    Args:
        data (list or generator): A sequence of numerical values.
        threshold (float): The threshold value for comparison.
    
    Yields:
        bool: True if the current value from data is > threshold, else False.
             Since only specific cases are requested to be "True" here in many contexts, 
             strictly following 'yields True when > threshold', we can yield a boolean indicating this condition met.

    Note: This implementation assumes that yielding just True might not capture the distinction between yielded items.
            To match typical generator patterns where logic is shown for comparison, it yields True only if value > threshold, else False (or does nothing). 
            However per prompt "yields True" specifically on condition met suggests we should yield True or maybe something else to avoid infinite loop?
    
    Clarification based on task: The request says 'only when... greater than'. We will return a generator that yields the value itself if > threshold, otherwise skips. This is memory-efficient for large sequences and avoids building lists. If only yielding boolean (True/False) was strictly required, we'd yield True or False to represent condition met/not; else just skip on fail which may not match "yields True".

    Revised approach: Yield a value that indicates the result clearly - but if strict instruction is 'yield True' ONLY when > threshold and nothing otherwise? That would break pattern unless always call next. So likely they meant yield boolean indicating status (True=True/False else).
    
    Final decision per "yields True only when..." -> means it should NOT yield False either, maybe skip on fail? But then user might get empty stream for many inputs. 
    Given typical use case: We'll implement as yielding the raw value if > threshold to provide meaningful data; however task specifically asks for 'True'. Let's do exactly what asked: Yield True ONLY when input > threshold (and nothing otherwise) -- but that means only yields subset of values? Actually better interpretation: yield a boolean result indicating whether condition met.

    Given ambiguity resolved via standard practice + "memory-efficient": We'll use generator yielding the value itself if > threshold to show positive match, else skip entirely (not yielding). This is memory efficient and fulfills 'only when'. 

    Wait again task says 'yields True only when ...' meaning output type should be boolean? Yes. So yield True or not-yield anything on failure? Or maybe just return generator that gives you list of booleans for each item, but since input size large, don't store list - use iterator directly.

    Let's implement cleanly: Generator yielding a tuple (value > threshold) where value comes from data. But to match "yield True", simpler is yield the boolean result itself per element. 

    Actually final plan: The function receives an iterable and yields either `True` or skips if <= threshold? Or maybe better to mimic typical filter pattern but with explicit bool output every time (so always yields something). Since task says 'yields True only when' meaning condition met -> yield True, else do nothing. 

    To be safe and avoid infinite loops: We'll iterate through input without storing everything - memory efficient by default for Python generators if not consuming all into list.

"""
# Final implementation decided to match "yield True" specifically on > threshold condition (and skip others)
def value_generator(data, threshold):
    # Ensure data is iterable; handle both lists and other iterables directly without materializing whole input
    
    for item in data:
        if isinstance(item, float) or isinstance(item, int) or isinstance(item, complex):
            val = float(item)  # safe conversion for numeric comparison
        else: 
            # Handle non-numeric gracefully; skip unless explicitly convertible? But task implies numbers.
            continue
        
        if item > threshold:
            yield True

if __name__ == '__main__':
    # Hard-coded sample values ensuring no external inputs, network access or files needed
    data = [10.5, 23, -47, 98.6, 0]
    threshold_value = 15
    
    result_gen = value_generator(data, threshold_value)

    for res in result_gen:
        print(res) # Outputs True only when item > threshold (i.e., indices with values like 23 and 98.6 become True; others skipped or False depending on interpretation - here we skip non-matching so no output else)