import sys

def main():
    # Retrieve two numerical values from command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python script.py <value_a> <value_b>")
        return
    
    try:
        value_a = float(sys.argv[1])
        value_b = float(sys.argv[2])
        
        # Compare and output result
        if value_a > value_b:
            print('Value A is larger')
        elif value_b > value_a:
            print('Value B is larger')
        else:
            print("Values are equal")
    except ValueError as e:
        print(f"Error: Invalid numeric input. {e}")

if __name__ == '__main__':
    # Hard-coded sample values to run without user interaction
    import subprocess
    
    if len(sys.argv) != 3:
        # Simulate command-line args with hardcoded values for testing
        sys.argv = ['script.py', '10.5', '7']

    main()