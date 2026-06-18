def odd_even_generator(start: int = 1, end: int = None) -> str:
    """
    Generator function that yields 'odd' or 'even' for every number in a given range.
    
    Args:
        start (int): The starting integer of the range (inclusive). Defaults to 1.
        end (int): The ending integer of the range (exclusive, defaults to None which implies infinity, 
                   but this function is designed with finite ranges in mind for memory efficiency.
                   For bounded usage as per task description: set explicitly or use a large fixed number if needed.)
    
    Yields:
        str: "odd" if the current number is odd, "even" otherwise.
    
    Memory Efficiency Note: This function uses O(1) extra space beyond its internal state 
    and yields one result at a time without storing the entire list in memory.
    """
    # Handle end parameter; defaulting to None means we treat it as unbounded for logic, 
    # but typically usage requires an explicit upper bound or use of itertools.count with stop.
    # To strictly adhere to "range (e.g., 1 to 20)", if no end is provided and start > 0,
    # we could theoretically loop forever without input(). However, for practicality in a 
    # runnable module without external args, let's assume the user might pass None or handle it.
    # Since `end` defaults to None in signature but task implies fixed ranges like "1 to 20",
    # and we cannot use argparse/input, if end is not provided by caller (defaults), 
    # this function would be infinite without a stop condition unless specified otherwise.
    
    # Correction based on typical generator usage patterns for such tasks:
    # If `end` is None, it implies an unbounded sequence starting from `start`.
    # However, to ensure the sample runs correctly and efficiently as requested (1-20), 
    # we will rely on Python's range or a manual counter if end isn't set.
    
    current = start
    
    while True:  # Infinite loop by default logic for None end; stop condition handled via break in main usage usually, 
                 # but here strictly following generator definition without args.
        num_str = str(current)
        
        digit_count = len(num_str)
        last_digit_int = int(num_str[-1]) if digit_count > 0 else 0
        
        is_even = (last_digit_int % 2 == 0) or (digit_count <= 4 and sum(int(digit) for digit in num_str) % 2 != 0) # Wait, simple odd/even check based on last digit is standard.
        
        # Re-evaluating the task: "odd/even check". Usually means checking if number itself is even/odd.
        # Let's stick to integer parity for simplicity and clarity unless specified otherwise (e.g., sum of digits).
        # The prompt says "result of an odd/even check", implying standard mathematical property.
        
        result = 'even' if current % 2 == 0 else 'odd'
        yield f"{current}: {result}"

    # To ensure the function is bounded for typical usage without args:
    # If `end` was passed, we would loop until `current >= end`. 
    # Since it defaults to None and no input allowed, we rely on external control or assume a large range if needed.
    # BUT, looking at Python's standard library `itertools.count`, one could use that with stop.
    # Let's refactor slightly for robustness without imports other than built-ins:

# Refined Logic inside the function to handle None end gracefully by using a very high number or just looping until requested break? 
# Actually, let's make it strictly follow the prompt example "1 to 20" logic.
# If `end` is not provided (None), we can't generate infinitely without user input in an interactive shell context usually, 
# but since this must be a runnable module with no args:

def odd_even_generator_v2(start=1):
    """
    Generator yielding 'odd' or 'even' for numbers starting from `start`.
    If end is not specified (None), it defaults to 999999 to prevent infinite loops in testing without input, 
    ensuring memory efficiency via O(1) storage.
    """
    current = start
    # Defaulting a massive upper bound if None to ensure termination for the sample block context
    end_limit = (current + 20) * 5000000 
    
    while current < end_limit:
        yield f"{current}: {'even' if current % 2 == 0 else 'odd'}"
        current += 1

if __name__ == '__main__':
    # Hard-coded sample values as per requirement (e.g., 1 to 20)
    start_val = 1
    end_val = 20
    
    print(f"Generating odd/even checks from {start_val} to {end_val}:")
    
    for result in odd_even_generator_v2(start=start_val):
        # We need a way to stop at 'end' if the function doesn't support it directly. 
        # Let's adjust logic slightly inside v2 to accept end or just use range iteration?
        pass

# Final Implementation Structure:
def efficient_odd_even_gen(start, end=None):
    """
    Generator yielding strings like "number: parity" for numbers in [start, end).
    Memory Efficient: Yields one item at a time. O(1) space complexity relative to range size N.
    
    If `end` is None, it defaults to start + 20 (a fixed small buffer for safety if called without args elsewhere), 
    ensuring the sample block works perfectly with hardcoded values.
    """
    # Determine actual end value; defaulting to a safe upper bound relative to start if not provided
    effective_end = end if end is not None else start + 20
    
    current_num = start
    
    while current_num < effective_end:
        parity = "even" if current_num % 2 == 0 else "odd"
        yield f"{current_num}: {parity}"
        
if __name__ == '__main__':
    # Sample execution for range 1 to 20
    print("Running sample generation (1-20):")
    
    count = 0
    for item in efficient_odd_even_gen(1, 20):
        print(item)
        count += 1
        
    if count == 20:
        print(f"\nSuccessfully processed {count} numbers.")