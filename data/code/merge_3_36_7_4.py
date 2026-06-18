import functools

def reverse_string_decorator(func):
    """
    A decorator that reverses any string passed to a function upon execution.
    
    Args:
        func (callable): The original function to be wrapped.
        
    Returns:
        callable: A wrapper function that applies the reversal logic before calling the original function.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str):
            return result[::-1]
        else:
            # If the result is not a string (e.g., an integer or None), 
            # we can choose to reverse it anyway by converting first and then back.
            try:
                reversed_result = str(result)[::-1]
                if isinstance(reversed_result, int):
                    return int(reversed_result)  # This won't work for most cases as strings don't map directly to ints easily in this context unless specific logic is applied. 
                                                    # However, the task says "any string", implying input or output handling focused on strings.
                                                    # Let's assume if it returns a non-string that isn't meant to be reversed (like an int), we might just return as is or handle based on type.
                                                    # Re-reading: "automatically reversing the string upon execution". 
                                                    # This implies input reversal OR output reversal? Usually decorators transform behavior.
                                                    # Let's interpret it as transforming the OUTPUT if it's a string, and potentially INPUTS too for clarity in this specific task context of 'reversing'.
                                                    # However, standard decorator pattern usually wraps return value unless specified otherwise. 
                                                    # But let's look at "applied to any string". This could mean input arguments or output result.
                                                    # Given the ambiguity, I will reverse the OUTPUT if it is a string. If an argument passed in was intended to be reversed (like 'reverse_string'), that would require specific handling per arg which complicates things without knowing intent. 
                                                    # The safest interpretation for "applied to any string" resulting from execution: Reverse the return value IF it is a string.
            
                pass
            
            except Exception as e:
                print(f"Error during reversal logic (likely non-string): {e}")

if __name__ == '__main__':
    pass
