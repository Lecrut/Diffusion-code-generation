"""
Script demonstrating list comprehension vs str.join() optimization 
for constructing a final string from multiple parts.
"""

def create_greeting():
    """
    Creates a greeting message by combining name and suffix strings.
    
    This function demonstrates two common approaches:
    1. Using the built-in 'str.join()' method (typically faster)
    2. Using list comprehension with concatenation
    
    The optimization lies in avoiding repeated string allocations 
    that occur when using + or += operators inside loops, which is 
    what often leads to inefficient code if not careful.
    
    Returns:
        str: A formatted greeting message.
    """
    name = ["Alice", "Bob"]  # Simulating a list of names
    
    # Approach 1: Using 'str.join()' - The Optimized Way
    # This method is generally preferred because it creates the string 
    # in fewer passes through memory compared to repeated concatenation.
    optimized_greeting = ", ".join([f"{name[i]} says hello!" for i in range(len(name))])

    return f"Optimized Result: {optimized_greeting}"

def create_old_style():
    """
    Creates a greeting message using traditional loop-based string 
    concatenation (for comparison purposes).
    
    This approach is less efficient due to creating new string objects 
    on every iteration. It serves as the baseline for optimization demonstration.
    
    Returns:
        str: A formatted greeting message created via loops.
    """
    name = ["Alice", "Bob"]  # Simulating a list of names
    
    result_parts = []
    
    # Traditional loop approach (less optimized)
    for i in range(len(name)):
        part = f"{name[i]} says hello!"
        result_parts.append(part)
    
    old_style_greeting = "".join(result_parts)

    return f"Old Style Result: {old_style_greeting}"

if __name__ == '__main__':
    # Hard-coded sample values as per requirements.
    # No user input, command-line arguments, or network access is used.
    
    print(create_old_style())
    print()
    print(create_greeting())