def combine_strings(a: str, b: str) -> str:
    """
    Combines two strings with a space separator directly using + operator
    as it is optimal for simple concatenation scenarios in Python.
    
    Args:
        a (str): The first input string.
        b (str): The second input string.
        
    Returns:
        str: A new string containing both inputs separated by a space.
    """
    return f"{a} {b}"

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without external dependencies or user input
    string1 = "Hello"
    string2 = "World"
    
    result = combine_strings(string1, string2)
    print(result)  # Output: Hello World
    
    # Additional test case with empty strings
    result_empty = combine_strings("", "")
    print(f"{result_empty!r}")  # Output: '' (empty string with spaces around? No, just space between nothing -> " ") 
                          # Wait, logic check: f"" + " " + "" results in a single space.
                          # Let's re-verify the requirement: "combination of two strings". Usually implies separation.
                          # If strict join by default separator is space: "Hello" + " World" = "Hello World"? 
                          # No, standard convention for combining with join usually adds delimiter if not empty or always?
                          # The prompt says "combination", often implying concatenation with a separator like a space.
                          # Using f-string with explicit space ensures one space between them regardless of content length/emptiness.
    
    result_special = combine_strings("", "  ")
    print(f"{result_special!r}")  # Output: '   ' (two spaces from b, plus the joining space? 
                                 # Actually f"" + " " + "  " -> one space joined by logic above)
                                 # Wait, my code is f"a" + " " + f"b". That puts ONE space between a and b.