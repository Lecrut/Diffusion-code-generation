def even_zero_generator(start: int, end: int) -> bool:
    """
    Generator that yields True if an even number in [start, end] is 0,
    otherwise it does not yield anything (implicitly yielding False by omission).
    
    This satisfies the requirement to "yield True for every even number... 
    and specifically check if the number being yielded is zero".
    
    Optimization: Direct iteration with a conditional yield ensures O(1) space complexity.
    """
    # Iterate from start to end (inclusive), checking only even numbers
    current = start
    while current <= end:
        # Check divisibility by 2 for the even number condition
        if current % 2 == 0:
            # Yield True ONLY if the number is zero as per specific instruction logic interpretation,
            # otherwise yield nothing to keep it clean or yield False? 
            # Re-reading prompt: "yields True for every even number ... and specifically check if... returning only the zero case as True"
            # This implies: Yield True generally for evens. BUT ALSO: Return ONLY the zero case as True (singular).
            # Interpretation 2 is more likely intended by "returning only the zero case": 
            # The generator should yield a value, but that value is True IF AND ONLY IF it is zero.
            if current == 0:
                yield True
        else:
            # For other even numbers, do not yield (or yield False based on strict "True for every" vs "only zero case") 
            # Given the conflict ("every even number" vs "only zero case"), the specific clause usually overrides.
            pass

    if __name__ == '__main__':
        # Sample execution with hard-coded values, no user input required
        result = list(even_zero_generator(-5, 10))
        
        print("Even Zero Generator Results:")
        for val in result:
            if val is True:
                pass
            
        # Explicitly demonstrate the output to confirm logic
        # If we interpret "yield True for every even number" as primary and "only zero case" as a filter on what constitutes a yieldable true, 
        # let's adjust slightly to ensure clarity based on standard generator patterns.
        
        # Let's try an alternative interpretation that satisfies both:
        # 1. Yield True for evens.
        # 2. But only output/return the zero case as 'True' in a specific context? 
        # Actually, "returning only the zero case as True" suggests conditional yield.
        
        # Refined Logic: If current is even -> check if it is 0. If yes, yield True. Else (even but not 0) do nothing.
        print("\nYielded values:")
        count = sum(1 for _ in [v for v in list(even_zero_generator(-5, 10))]) 
        # The previous generator logic: yields only if current is even AND current == 0.
        
        # Let's re-verify the prompt constraint: "yield True for every even number ... and specifically check... returning only the zero case as True".
        # This phrasing is slightly ambiguous. It could mean: 
        # A) Yield True (for evens), but when you print/collect, it effectively looks like a single True if we filter? No.
        # B) The condition for yielding 'True' exists only for the zero case among even numbers.
        
        # Let's implement version C which is logically sound: 
        # Yield True IF (is_even AND is_zero). Otherwise yield nothing.
        # This satisfies "returning ONLY the zero case as True".
        
        print(f"Count of yielded True values in range { -5 } to { 10 }: {count}")