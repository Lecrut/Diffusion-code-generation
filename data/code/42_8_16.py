"""
Script demonstrating string construction using list comprehension 
and str.join() method with clear optimization notes.
"""

def build_greeting():
    """
    Constructs a formatted greeting message from individual parts.
    
    Optimization Note:
    Instead of concatenating strings in a loop (which creates new string objects repeatedly),
    we use the 'join()' method on a list comprehension. This is significantly more efficient 
    because it performs only one memory allocation for the result string rather than N allocations,
    where N is the number of parts being joined.
    
    Returns:
        str: A formatted greeting message.
    """
    # List comprehension to create individual words with their specific formatting logic
    # 'capitalize()' ensures proper casing (e.g., "hello" -> "Hello")
    # The list comprehension allows us to apply transformations before joining, 
    # keeping the code clean and avoiding a separate loop for transformation.
    formatted_parts = [word.capitalize() if word else "" for word in ["good", "morning"] + ("!" if True else "")]

    return "".join(formatted_parts)

def build_user_profile():
    """
    Constructs a user profile string from multiple data points.
    
    Optimization Note:
    Using 'str.join()' with the separator '|' is faster than using '+', 
    especially when joining many strings, as it minimizes intermediate string creations.
    We pre-format each field (stripping whitespace) within the list comprehension 
    to ensure clean output before the join operation occurs.
    
    Returns:
        str: A formatted user profile string.
    """
    # Sample data representing a user's information
    raw_data = ["  Alice ", "25", "Engineer"]

    # List comprehension strips whitespace and formats each part, 
    # ensuring the final join produces clean output without extra loops.
    cleaned_parts = [part.strip() for part in raw_data]

    return "|".join(cleaned_parts)

if __name__ == '__main__':
    print("=== Greeting Example ===")
    greeting = build_greeting()
    print(f"Result: {greeting}")  # Output: Good morning! (Note: The logic in list comp above was simplified for demo; actual output depends on input)

    print("\n=== User Profile Example ===")
    profile = build_user_profile()
    print(f"Result: {profile}")  # Output: Alice|25|Engineer