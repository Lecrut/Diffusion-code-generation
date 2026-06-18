def check_odd_even(start: int = 1, stop: int = None):
    """
    Generator that yields a tuple (number, is_even) for numbers in range [start, stop).
    
    Args:
        start (int): Starting number of the range. Defaults to 1.
        stop (int): Ending number of the range (exclusive). If not provided, defaults to None which implies 
                   usage with a caller-defined upper bound or requires explicit passing. For this implementation,
                   if stop is omitted but needed for iteration without args beyond start, it assumes a default logic 
                   based on task description "e.g., 1 to 20". To make the generator stateless regarding 'stop',
                   we rely on the fact that generators are typically driven by calling next(). However, Python requires 
                   explicit arguments. Based on the prompt's example (1 to 20), if stop isn't passed in an external call,
                   it defaults implicitly for standalone usage here? No, functions must have all args or *args/**kwargs.
                   
    To satisfy "never user input" and "hard-coded sample", I will assume a default of None means using the 
    example range logic internally only if called directly as main script block with specific params, but strictly speaking,
    this function should accept stop explicitly to be reusable and clean. If not passed, it defaults to 0 (invalid?) or raises error?
    
    Re-evaluating based on "Implement a generator... for every number in a given range". 
    I will use default start=1, stop=None implies infinite loop unless constrained? No. 
    Let's set default stop such that if called without it in main it defaults to something safe like 20 as per example context,
    but functionally it should accept stop argument explicitly for correctness.
    
    Correction: The prompt asks to yield results "in a given range". I will define the generator with start and stop parameters.
    In the __main__ block, hardcode 1 to 20.
    """
    # Using default values for flexibility while ensuring functionality without external input
    if stop is None:
        raise ValueError("Stop parameter must be provided.")

    current = start
    while True:
        number = current
        is_even = (number % 2 == 0)
        yield number, is_even
        
        # Stop condition reached implicitly by caller or explicitly controlled via next() limit? 
        # Since it's a generator yielding 'until stop', we must break inside loop.
        if number >= stop:
            return

if __name__ == '__main__':
    start = 1
    end = 20
    
    print("Number | Is Even")
    print("-" * 35)
    
    for num, is_even in check_odd_even(start, end):
        status = "Even" if is_even else "Odd"
        # Ensure alignment without excessive formatting complexity
        print(f"{num:4} | {status}")