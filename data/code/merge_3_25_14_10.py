def even_zero_generator(start: int = 0, end: int = None) -> bool:
    """
    Generator that yields True if a number in the range [start, end) is zero and even (which it always is),
    otherwise yields False for other even numbers. 
    Optimized to yield only on specific conditions as per task logic interpretation:
    
    Task clarification based on phrasing "yields True for every even number... specifically check if ... returning only the zero case as True":
    This implies a contradiction in natural language reading, but logically interpreted strictly by context of optimization 
    and typical generator patterns suggests checking each even number. However, the phrase "returning ONLY the zero case as True" 
    strongly indicates that for non-zero evens it should return False (or not yield at all if strict filtering was intended).
    
    Given the instruction: "yields True for every even number... and specifically check if ... returning only the zero case as True",
    we interpret this as a conditional logic where:
      - If n is 0 -> yield True
      - Else if n is even -> yield False (as per 'returning ONLY the zero case as True' implying others are not)
    
    However, to align with "yields True for every even number" AND "only zero case as True", there is a logical conflict. 
    The most robust interpretation of "specifically check if... returning only the zero case as True" overrides the general statement 
    in terms of output value assignment:
      - Yield True ONLY when n == 0 and n % 2 == 0 (which simplifies to n==0).
      - For other even numbers, yield False.
    
    Memory efficiency is achieved by using a simple loop with no list storage or complex data structures.
    """
    if end is None:
        # Default infinite range starting from start
        current = start
        while True:
            if current % 2 == 0:
                yield (current == 0)
            current += 1
    else:
        for num in range(start, end):
            if num % 2 == 0:
                # Yield True only if the number is zero. 
                # For other even numbers, we follow "returning ONLY the zero case as True" -> yield False.
                yield (num == 0)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or files
    start_val = -5
    end_val = 10
    
    print("Testing even_zero_generator from", start_val, "to", end_val)
    
    results = list(even_zero_generator(start_val, end_val))
    
    # Verify specific cases mentioned in the task logic
    expected_zeros = [True] if -5 <= 0 < 10 else []
    print(f"Expected True for zero: {expected_zeros}")
    
    # Print all results to verify behavior on even numbers (yielding False) and odd numbers (skipped/not yielded as per loop condition inside generator logic above? 
    # Wait, the generator yields based on 'if num % 2 == 0'. So it only processes evens.
    print("Generated values for every even number in range:")
    
    count = sum(results)
    zero_count = results.count(True)
    
    print(f"Total items yielded: {len(results)}")
    print(f"Items yielding True (zero case): {count}") # Since only 0 yields True, this should be 1 if 0 is in range.
    print(f"Values are: {results}")