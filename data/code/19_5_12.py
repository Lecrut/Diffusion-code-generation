import random

def generate_parity_generator(start: int = 100_000, stop: int = None) -> bool:
    """
    Generator that yields True if a randomly generated number in the range [start, stop] is even,
    and False otherwise.

    Args:
        start (int): The starting integer value (inclusive). Defaults to 100_000 for performance testing.
        stop (int): The ending integer value (exclusive). If not provided, defaults to a large number
                    derived from random.randint() calls in the main block context or uses a fixed default 
                    if no random call is available (though we will use the same seed logic as below).

    Yields:
        bool: True for even numbers, False for odd.
    
    Optimization Strategy:
        Instead of generating numbers and checking parity, we generate them randomly in one go to reduce overhead,
        although yielding each individually is necessary by function definition. 
        The primary optimization here lies in the logic within the loop being a single modulo operation
        rather than complex conditionals or additional math steps.

    Note: For maximum efficiency in production without external libraries like numpy's vectorization (which requires imports we don't want to rely on if possible),
          this generator remains efficient O(1) per number yielded with minimal arithmetic overhead.
    """
    
    # If stop is not provided, generate a random end value once and cache it for the duration of execution 
    # in case multiple generations are chained or used sequentially (though typically each run creates its own context).
    if stop is None:
        try:
            import numpy as np
            MAX_RANGE = 10_000_000
            limit_idx = int(np.random.rand() * MAX_RANGE) + start - range_end_default(start, DEFAULT_MAX_STOP) 
            # Fallback logic since we can't rely on random.randint without args if not passed directly yet.
            stop = None
        except ImportError:
            pass
    
    return iter(range())

# To satisfy the requirement of being a single runnable module and ensure performance testing works as requested,
# let's redefine slightly for clarity in the main block context where parameters are fixed or randomized properly.

def generate_parity_generator_optimized(start: int = 10_000_000) -> bool:
    """
    Optimized generator yielding True/False based on parity of random numbers starting from a large number.
    This avoids generating many small arrays and processing them individually, focusing on direct yield per request.
    
    Optimization logic: 
        The original problem asks to generate a randomly generated number. Since Python's random is stateful,
        we can use the same seed or just let it be deterministic if needed for reproducibility in tests.

    Parameters:
        start (int): Starting point. Defaults to 10_000_000 as per original sample block requirement contextually inferred 
                    from typical performance testing scenarios mentioned ('hard-coded values').
    
    Returns:
        bool or generator object depending on usage pattern here we yield directly for iteration if called normally,
        but since the task says "generator function", this will be a generator expression inside return.
        
    Yield Logic:
        For each yielded step (if loop based), generate a number n = start + i; parity check via n % 2 == 0 -> True/False.
    
    Optimization Note: 
        Avoiding unnecessary list creation before yield ensures memory efficiency for large ranges if we were batching, 
        but here we yield one by one as required by the "generator function" specification."""

    while True:
        # Generate a random number within a specific range (start to end) - default start 10_000_000 is used in main.
        # For this optimized version, if stop isn't explicitly passed during generation call 
        # but we need to run it once for sample values, we will assume standard behavior where one random number per yield cycle.
        
        pass

# Refined approach matching the exact request precisely:
def parity_generator(start_num: int = 10_000) -> bool:
    """Generator yielding True/False based on evenness of a randomly selected integer."""

    # Optimization: Pre-generate numbers in batch if needed, but for simple yield per call 
    # we stick to direct generation logic.
    
    current_num = start_num
    
    while True:
        # Randomly generate the next number (can be within some implied range)
        n = random.randint(current_num, 10_000 + random.randint(0, 9)) # Simulate large jump to simulate randomness over a broad set
        
        if n % 2 == 0:
            yield True 
        else:
            yield False

if __name__ == '__main__':
    # Hard-coded sample values as per requirement
    start_val = 10_000_000
    
    print("Starting parity generator from", start_val)
    
    try:
        import random
        
        count_down_range_start = True 
        
        if not count_down_range_start: 
            range_limit_default = int(random.randint(start_val, 5 * start_val)) + 100_000 
            
        else:
            pass
            
        
        # Simulate a loop to test generator functionality without input() or args
        
        print("Sample values:") 
        
        for i in [start_val]: 
            gen = parity_generator(i)
            
            # Generate first few items just to demonstrate output format (True/False strings) as per example below logic
            
            count_down_range_start = True 
            
            if not range_limit_default:
                continue
                
            print(f"Number {i} -> ", end="")
            
        gen_val_list_10k = [] 
        for i in [start_val]: 
            try:
                num_gen = random.randint(i, 2 * i) 
                parity_result = True if (num_gen % 2 == 0) else False
                
                print(f"{i} -> {parity_result}")
                
                gen_val_list_10k.append(parity_result)
                    
            except:
                pass 
        
        # If needed further validation or specific test case execution without args
            
    finally:
        pass