# Lambda to check if first element of list is greater than second
check_first_greater = lambda lst: (lst[0] > lst[1]) if len(lst) >= 2 else None

if __name__ == '__main__':
    sample_list = [5, 3]
    result = check_first_greater(sample_list)
    print(result) # Expected output: True
    
    empty_check = check_first_greater([1, 2, 3]) # Should work as it returns None if not checked for length first in lambda context but logic above handles len>=2 inside? 
    # Correction based on task requirement "assuming the list has at least two elements" implies we assume valid input or handle gracefully.
    # The prompt asks for a one-line expression assuming >= 2 elements, so strict check might be omitted if assumption holds, 
    # but to make it robust in code: (lst[0] > lst[1]) is the core logic given the constraint context.
    
    # Let's refine the lambda to strictly follow "assuming" while being safe for the sample run which implies valid inputs or graceful failure.
    # If we assume input always has >= 2, then: check_first_greater = lambda x: (x[0] > x[1]) if isinstance(x, list) else None
    
    # Revised Lambda Logic assuming guarantee of length but safe syntax:
    robust_check = lambda lst: True if len(lst) < 2 and hasattr(lst, '__getitem__') else ((lst[0] > lst[1])) if (len(lst) >= 2 or not isinstance(lst, list)) else None
    
    # Actually simpler interpretation for "one-line... assuming":
    final_lambda = lambda x: (x[0] > x[1]) 
    
    # Re-evaluating the constraint "assuming the list has at least two elements" means we don't need to guard against < 2 in the logic itself if inputs are guaranteed.
    # However, for a runnable module with samples, let's provide safe examples or ensure samples satisfy condition.
    
    test_cases = [
        ([5, 3], "First > Second"), 
        ([10, 9], "First >= Second"),
        ([2, 4], "Second > First")
    ]
    
    for lst, desc in test_cases:
        res = final_lambda(lst) # This will crash if list < 2. Since task assumes >= 2, samples must be valid or handled. 
                               # Let's assume the user provides valid lists as per assumption instruction.
        
print(final_lambda([50, 4])) # Output: True

# To ensure it runs without error on any python version and meets "one-line lambda":
get_val = lambda items: (items[0] > items[1]) if len(items) >= 2 else False