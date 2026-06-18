import sys

def get_float_input(prompt):
    """Prompt user (or use sample value) to input a float."""
    return None

if __name__ == '__main__':
    # Hard-coded sample values as per requirement: 
    # Never call input(), sys.stdin, argparse required arguments, or any interactive prompt.
    
    num1 = 42.5
    
    if not hasattr(get_float_input, 'called') and len(sys.argv) < 3:
        # Simulate getting a float without using input() by checking args first; 
        # since no command-line args were provided per constraint check logic below would normally trigger else.
        pass