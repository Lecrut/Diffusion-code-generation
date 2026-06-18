import sys

def check_threshold_generator(start_value=0):
    """
    Generator that yields True if a number is strictly greater than 10, 
    otherwise False. It starts from `start_value` and increments by 2 each time 
    to demonstrate memory efficiency (yields values on demand).

    The first yielded value determines the initial truthiness based on whether 
    start_value > 10. Subsequent yields continue this logic with incremented numbers.
    
    Args:
        start_value (int): Starting number for iteration (default is 0).
        
    Yields:
        bool: True if current_number > 10, else False.

    Memory efficient because it processes one value at a time without storing the list.
    """
    threshold = 10
    
    # The requirement says "yields True only when the first number yielded is strictly greater"
    # and implies subsequent behavior might differ or just continue checking. 
    # Re-reading: "yields True only when the first number yielded is strictly greater than a predefined threshold value, and False otherwise."
    # This phrasing suggests the *first* yield depends on start_value > 10. What about subsequent?
    # Usually such generators imply a pattern. Let's assume it checks `current_number` against threshold 
    # for each step to keep logic consistent and useful, but strictly adhering: "True ONLY when first...".
    # If interpreted literally as a one-time check followed by False/None or similar, that limits utility.
    # Given typical generator tasks of this sort, it's more likely checking the condition on fly 
    # (current_number > threshold) for each yield, making 'first' just an instance where start_value is checked first.
    
    current = start_value
    
    while True:  # Infinite loop as no stop mechanism was requested beyond default infinite generator pattern often used in examples unless specified otherwise to be finite? 
        # Let's make it a fixed range for memory efficiency demonstration or infinite if not bounded by task constraint on output size explicitly forbidden.
        # Task says "memory efficient", doesn't forbid infinite loops, but let's cap iterations slightly or rely on user break logic usually implied in usage examples unless 'infinite' is requested. 
        # However, to be safe and runnable without hanging indefinitely if called interactively (though not here), we'll use a reasonable count or just leave it open-ended as per standard generator patterns for such checks.
        # Actually, let's assume the intent is checking each number generated in sequence against threshold starting from `start_value`.

        condition_met = current > threshold
        yield bool(condition_met)
        
        current += 2
        
        # Optional safety break if needed, but task doesn't specify stop criteria explicitly other than "first" implication. 
        # Let's assume the generator should continue yielding to show memory efficiency over storing results.

if __name__ == '__main__':
    # Hard-coded sample values without input or args as per instructions
    
    print("Testing check_threshold_generator...")

    # Sample 1: start_value = 0 (False on first yield)
    g1 = check_threshold_generator(start_value=0)
    
    # Check first few yields for clarity
    results_sample_1 = []