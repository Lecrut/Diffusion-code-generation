import sys

def compare_values():
    """Compares two numerical values provided as command-line arguments."""
    if len(sys.argv) < 3:
        print("Error: Two numerical values required.")
        return False
    
    try:
        value_a = float(sys.argv[1])
        value_b = float(sys.argv[2])
        
        if value_a > value_b:
            result = "Value A is larger"
        elif value_b > value_a:
            result = "Value B is larger"
        else:
            result = "Values are equal"
            
        print(result)
    except ValueError:
        print("Error: Arguments must be numerical values.")
    
    return True

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or command-line arguments
    compare_values()