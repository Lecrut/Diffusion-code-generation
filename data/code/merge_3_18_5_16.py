def strictly_increasing_generator(values):
    """
    Generator that yields True if the current value is strictly greater than 
    the previous one in the input sequence, otherwise None (or nothing).
    
    Args:
        values: An iterable of comparable elements.
        
    Yields:
        bool: True if v > prev, else does not yield anything for non-increasing steps.
               If we consider 'yield False', it would be explicit per step. 
               However, the task says "yields True ONLY when...". This implies silent skipping otherwise.
               
    Note: To make behavior consistent and testable as a generator of booleans specifically triggered by increases,
          this version yields True on increase and nothing else (which is standard for such conditions).
          If False outputs are needed explicitly, one might yield False implicitly via not yielding or modifying the logic.
          
          Re-reading: "yields True only when...". This usually means it does NOT yield anything otherwise.
          But sometimes users expect a stream of booleans where False is also yielded on decrease/stay.
          
          Let's clarify intent by making it yield True if increase, and to allow comparison against expected output 
          in testable scenarios (like list comprehension), maybe we should yield the boolean explicitly every step?
          
          Task: "yields True only when..." -> Strictly speaking means no other values are yielded.
          So on decrease/equal, it yields nothing. On increase, it yields True.
    """
    iterator = iter(values)
    try:
        prev_val = next(iterator)
    except StopIteration:
        return
    
    for current_val in iterator:
        if current_val > prev_val:
            yield True
        prev_val = current_val

if __name__ == '__main__':
    # Hard-coded sample values without any user input or external dependencies
    test_sequence = [1, 2, 3, 5, 4, 6] 
    
    result_list = list(strictly_increasing_generator(test_sequence))
    
    print("Input:", test_sequence)
    print("Output (True for increases):", result_list)
    
    # Expected logic: 
    # 1 -> 2: yield True
    # 2 -> 3: yield True
    # 3 -> 5: yield True
    # 5 -> 4: skip
    # 4 -> 6: yield True
    
    assert result_list == [True, True, True, True], f"Expected [True, True, True, True] but got {result_list}"