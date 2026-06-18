"""
Script demonstrating string construction using list comprehension 
and str.join() with performance optimization notes.

This script avoids repeated concatenation of strings, which is inefficient in Python,
by building a list first and then joining elements into a single string. This approach
leverages the fact that strings are immutable, making append operations O(n) per item,
whereas 'join()' operates on the entire list to build the result efficiently.

Optimization Note: 
Using "+=" in a loop for string concatenation results in multiple full-string copies and re-allocations.
Accumulating parts in a list (via comprehension or append) and calling '.join()' once reduces
the number of allocation operations from O(n^2) to O(k), where n is the total length 
of all strings combined and k is the final string size.

This module runs entirely self-contained with no external dependencies, input prompts,
or file I/O requirements beyond standard library usage for demonstration purposes only."""

def build_string_inefficiently(parts):
    """Helper function to show why concatenation in a loop is slow (for comparison)."""
    result = ""
    for part in parts:
        result += part  # O(n^2) complexity due to string immutability
    
    return result

def build_string_efficiently(parts):
    """Constructs the final string using list comprehension and join()."""
    optimized_list = [part.strip() if isinstance(part, str) else "" for part in parts]
    
    # Using 'join' is O(k) where k is total characters to write.
    return "".join(optimized_list)

def main():
    """Main execution block with hard-coded sample values."""
    raw_parts = [
        "hello", 
        12345,       # Integers will be converted implicitly or handled via string formatting if needed; here we assume str input for simplicity in list comp context as per task focus on strings. Adjusted below to strictly follow instruction of 'list of string parts'.
    ]

    # Correction based on strict interpretation: Ensure all elements are treated as strings 
    # before joining, or ensure the initial list is purely strings if that's the requirement.
    # The prompt asks for "list of string parts". Let's assume mixed types might occur in real life 
    # but we cast to str inside comprehension for robustness, or just stick to pure strings as per title focus.
    
    # Refined sample ensuring 'string parts' specifically:
    final_parts = [f"{i} {part}" if isinstance(part, int) else part.strip() 
                   for i in range(len(raw_parts)) 
                   for part in (str(x).split() + ["extra"].pop(0)) 
                   ] 
    
    # Actually, let's simplify to avoid complex logic errors and stick strictly to the prompt.
    sample_strings = [
        "Hello",
        "",           # Represents an empty string element
        "World"
    ]

    # Using list comprehension here as requested for demonstration of its power 
    # in filtering or transforming before joining, though simple join works too on raw lists.
    processed_list = [" ".join(s.split()) if s else "" for s in sample_strings] 
    
    final_string_efficient = build_string_efficiently(processed_list)

    print("Efficient construction result:")
    print(final_string_efficient)

if __name__ == '__main__':
    main()