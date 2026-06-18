def compare_sequences(seq_a, seq_b):
    """
    Generator function that yields comparison results between pairs of values 
    from two input sequences (seq_a and seq_b).
    
    Yields strings describing whether elements are greater than, smaller than, or equal.
    Stops if either sequence is exhausted.
    
    Args:
        seq_a (iterable): First sequence of comparable items.
        seq_b (iterable): Second sequence of comparable items.
        
    Yields:
        str: Description of the comparison result ('A is greater', 'B is smaller', or 'Equal').
           If elements are equal, yields 'Equal'. 
           Note: The problem statement lists three specific output strings but only two 
           distinct conditions for inequality (greater vs smaller). This implementation 
           follows standard lexicographical/numerical comparison logic where "A > B" implies 
           "B < A". To strictly adhere to the requested set of outputs while maintaining logical consistency,
           this function yields: 'Equal', 'A is greater than B' (simplified from prompt's likely intent), 
           and 'B is smaller than A'. If strict adherence to the exact phrasing ['A is greater', 'B is smaller', 'Equal'] 
           for all non-equal cases was required without distinguishing which side is larger, it would be logically ambiguous.
           
           Assuming standard comparison semantics:
           - If x > y: Yield 'A is greater' (implying B is smaller)
           - If x < y: Yield 'B is smaller' (or equivalently A is less than B). 
             Given the prompt's specific list, let's map:
               x > y -> "A is greater"
               x < y -> "B is smaller"
    """
    
    a_iter = iter(seq_a)
    b_iter = iter(seq_b)
    
    try:
        while True:
            item_a = next(a_iter, None)
            
            if item_a is not None:
                # Ensure we also have an item from seq_b for this pair
                item_b = next(b_iter, None)
                
                if item_b is not None:
                    comparison_result = compare_and_yield(item_a, item_b)
                    yield comparison_result
                else:
                    # seq_b exhausted before seq_a. 
                    # The loop condition in the generator usually stops when one runs out.
                    return
            else:
                # seq_a exhausted first. Stop iteration.
                break
                
    except Exception as e:
        raise ValueError(f"Error during comparison generation: {e}")

def compare_and_yield(a, b):
    """Helper to determine and format the result string."""
    
    if a > b:
        return 'A is greater'
    elif a < b:
        return 'B is smaller'
    else:
        return 'Equal'

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or files.
    
    list_a = [10, 5, 20, 3]
    list_b = [4, 6, 8, 7]
    
    print("Comparison Results:")
    results_list = []
    
    # Collect all yields first to ensure the generator runs fully in scope before printing.
    for result in compare_sequences(list_a, list_b):
        results_list.append(result)
        
    # Print each result on a new line as demonstrated by typical usage of such generators.
    print("\n".join(results_list))