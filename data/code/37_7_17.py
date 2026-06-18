def combine_strings(s1: str, s2: str) -> str:
    """
    Combines two strings efficiently using direct concatenation.
    
    For simple string combination tasks in Python where no intermediate 
    structures (like lists or arrays) are needed to be joined later, 
    the + operator is generally faster and more readable than list.append() 
    followed by join(). This function leverages that principle while maintaining 
    type safety through annotations.
    
    Args:
        s1 (str): The first input string.
        s2 (str): The second input string.
        
    Returns:
        str: A new string formed by concatenating s1 and s2 in order.
    """
    return f"{s1}{s2}"

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies
    sample_str_1 = "Hello"
    sample_str_2 = "World!"

    result = combine_strings(sample_str_1, sample_str_2)
    
    print(result)