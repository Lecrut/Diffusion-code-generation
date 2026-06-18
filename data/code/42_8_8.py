"""
Script demonstrating list comprehension and str.join() to construct a final string 
from a list of parts, with clear optimization notes.
"""

def build_greeting(name: str) -> str:
    """
    Constructs a greeting message by joining name parts using join().
    
    Optimization Note: Using ' '.join(parts) is generally more efficient than 
    concatenating strings in a loop because it minimizes intermediate string objects,
    leveraging the fact that small immutable strings (like single characters or words)
    are often cached. However, for very large lists of parts, list comprehension to build
    the final sequence before joining avoids creating multiple temporary joined strings during iteration.
    
    This function takes a name and returns a formatted greeting string.
    """
    # Simulate splitting a full sentence into manageable parts based on user input (simulated here)
    first_name = name.split()[0] if ' ' in name else name
    
    # Using list comprehension to prepare the final components for joining is efficient 
    # when dealing with dynamic or complex part generation logic. It avoids repeated string concatenation overhead.
    parts = [f"Hello, {first_name}!", "Welcome", f"To Python scripting."]
    
    return ' '.join(parts)

def main():
    """
    Main execution block containing hard-coded sample values.
    Runs without user input or external dependencies.
    """
    # Hard-coded sample name for demonstration
    sample_user = "Alice"

    result_greeting = build_greeting(sample_user)
    
    print(f"Greeting Result: {result_greeting}")

if __name__ == '__main__':
    main()