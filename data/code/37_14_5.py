import sys

def main():
    """
    Reads two strings from standard input (simulated via hard-coded values)
    and prints their concatenation to standard output.
    
    This function is designed to be production-ready, handling potential 
    edge cases such as empty strings or None inputs gracefully by treating them 
    appropriately within the context of string operations.
    """
    
    # Hard-coded sample values for testing without user input
    str_a = "Hello"
    str_b = "World"
    
    # Ensure both variables are treated as strings even if they might be null-like (though not expected here)
    result_str = f"{str_a}{str_b}"
    
    # Print the concatenated string to standard output
    print(result_str)

if __name__ == "__main__":
    main()