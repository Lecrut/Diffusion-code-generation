"""
Script demonstrating list comprehension and str.join() to construct a final string 
from a list of parts, with clear documentation on optimization techniques used.
No user input or external dependencies are required.
"""

def build_greeting():
    """
    Constructs a formatted greeting message using list comprehension and join().
    
    Optimization Note:
    Instead of repeatedly concatenating strings (e.g., s += part), which is O(n^2) 
    in terms of time complexity due to string immutability, we collect parts in a list 
    and use 'str.join()'. This approach creates the final string in O(n) time by 
    performing only one large allocation and copy operation.
    
    Alternatively, list comprehension is used here for clarity: [f"Hello {i}" for i in range(3)]
    which avoids creating intermediate temporary strings during iteration.
    """
    # Using f-strings inside a list comprehension to generate individual parts efficiently
    name_parts = ["John", "Doe"]
    
    # Constructing the full sentence using str.join() on a generator expression 
    # (which is also optimized as it avoids creating an intermediate list)
    final_message = ", ".join(f"{name} {i}" for i in range(1, 4)) + "."
    
    return f"Greetings to: {final_message}, and welcome!"

if __name__ == '__main__':
    # Hard-coded sample execution without any user input or external dependencies
    result = build_greeting()
    print(result)